from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from offices.models import Building, Office, Employee, Workplace_off, Reserved
import datetime


class BuildingListView(ListView):
    model = Building
    template_name = 'buildings_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['buildings'] = self.object_list
        return context


class OfficeListView(ListView):
    template_name = 'offices_list.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'

    def get(self, request, id):
        offices = Office.objects.filter(in_which_building_is_id=id)
        context = {
            'offices': offices,
        }
        return render(request, template_name='offices_list.html', context=context)


class Workplace_offListView(ListView):
    template_name = 'workplace.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'

    def get(self, request, id):
        workplaces = Workplace_off.objects.filter(which_office=id).order_by('which_office')
        for workp in workplaces:
            reservs_for_workp = Reserved.objects.filter(place_id=workp.id)
            if bool(reservs_for_workp) == False:
                workp.occupied = False
                workp.save()
            else:
                for reserv in reservs_for_workp:
                    if reserv.start_time <= datetime.date.today() <= reserv.end_time:
                        workp.occupied = True
                        workp.save()
                        break
                    else:
                        workp.occupied = False
                        workp.save()
        context = {
            'workplaces': workplaces,
        }
        return render(request, template_name='workplace.html', context=context)


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['employees'] = self.object_list
        return context


class EmploeeDetailView(DetailView):
    template_name = 'employee.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'

    def get(self, request, id):
        employee = Employee.objects.get(id=id)
        reservs = Reserved.objects.filter(who=id)
        context = {
            'employee': employee,
            'reservs': reservs,
        }
        return render(request, template_name='employee.html', context=context)


def create_reserved(request, id):
    if request.POST:
        res_list = Reserved.objects.filter(place_id=id)
        reserved = False
        for res in res_list:
            res_list_start = request.POST.get('start_time').split('-')
            res_list_end = request.POST.get('end_time').split('-')
            rds = datetime.date(int(res_list_start[0]), int(res_list_start[1]), int(res_list_start[2]))
            rde = datetime.date(int(res_list_end[0]), int(res_list_end[1]), int(res_list_end[2]))
            if (res.end_time < rds or rds < res.start_time) and (res.end_time < rde or rde < res.start_time):
                reserved = False
            else:
                reserved = True
        if reserved == False:
            Reserved.objects.create(
                who=Employee.objects.get(id=request.POST.get('who')),
                place=Workplace_off.objects.get(id=id),
                start_time=request.POST.get('start_time'),
                end_time=request.POST.get('end_time'), )
            employees = Employee.objects.all()
            return render(request, 'reserved_create.html', context={'employees': employees})
        else:
            return render(request, 'error_data_page.html')
    employees = Employee.objects.all()
    return render(request, 'reserved_create.html', context={'employees': employees})


class ReservedCreateView(CreateView):
    model = Reserved
    fields = ['place', 'who', 'start_time', 'end_time']
    template_name = 'reserved_create.html'


class SearchReservedPage(TemplateView):
    template_name = 'browse.html'


class SearchResultList(ListView):
    model = Workplace_off
    template_name = "day_reserved_workplace.html"

    def get_queryset(self):
        query_1 = self.request.GET.get('start')
        query_2 = self.request.GET.get('end')
        data_list_1 = query_1.split('-')
        date_start = datetime.date(int(data_list_1[0]), int(data_list_1[1]), int(data_list_1[2]))
        data_list_s2 = query_2.split('-')
        date_end = datetime.date(int(data_list_s2[0]), int(data_list_s2[1]), int(data_list_s2[2]))
        workplaces = Workplace_off.objects.all().order_by('which_office')
        for workp in workplaces:
            reservs_for_workp = Reserved.objects.filter(place_id=workp.id)
            if bool(reservs_for_workp) == False:
                workp.occupied = False
                workp.save()
            else:
                for reserv in reservs_for_workp:
                    if (reserv.start_time <= date_start <= reserv.end_time) or (
                                reserv.start_time <= date_end <= reserv.end_time):
                        workp.occupied = True
                        workp.save()
                        break
                    else:
                        workp.occupied = False
                        workp.save()
        return Workplace_off.objects.filter(occupied=False).order_by('which_office')
