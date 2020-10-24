from django.contrib import admin
from offices.models import Building, Office, Employee, Workplace_off, Reserved


class EmployeeAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'img')
    list_display = 'name', 'surname'
    list_filter = 'surname',


class BuildingAdmin(admin.ModelAdmin):
    fields = ('address', 'img')
    list_display = 'address',


class OfficeAdmin(admin.ModelAdmin):
    fields = ('in_which_building_is', 'office_number')
    list_display = 'in_which_building_is', 'office_number'

class Workplace_offAdmin(admin.ModelAdmin):
    fields = ('which_office', 'occupied', 'number_workplace')
    list_display = 'which_office', 'number_workplace'

class ReservedAdmin(admin.ModelAdmin):
    fields = ('place', 'who', 'start_time', 'end_time')
    list_display = 'place', 'who', 'start_time', 'end_time'



admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Building, BuildingAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Workplace_off, Workplace_offAdmin)
admin.site.register(Reserved, ReservedAdmin)





