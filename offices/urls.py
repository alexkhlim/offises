from django.urls import path

from offices.views import (BuildingListView,
                              OfficeListView,
                              Workplace_offListView,
                              EmployeeListView,
                              EmploeeDetailView,
                              create_reserved,
                              ReservedCreateView,
                              SearchReservedPage,
                              SearchResultList
                              )

urlpatterns = [
    path('buildings/', BuildingListView.as_view(), name='buildings_list'),
    path('offices/<id>', OfficeListView.as_view(), name='offices_list'),
    path('workplace/<id>', Workplace_offListView.as_view(), name='workplace_list'),
    path('employees/', EmployeeListView.as_view(), name='employees_list'),
    path('employee/<id>', EmploeeDetailView.as_view(), name='employee_detail'),
    path('reserved/<id>', create_reserved, name='reserved_create'),
    path('searchreserved/', SearchResultList.as_view(), name='search'),
    path('searchres/', SearchReservedPage.as_view(), name='sch')
]