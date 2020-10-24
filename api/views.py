from django.shortcuts import render

from django.shortcuts import render
from offices.models import Building, Office, Employee, Workplace_off, Reserved
from offices.serializers import EmployeeSerializer, BuildingSerializer, Workplace_offSerializer, ReservedSerializer, OfficeSerializer
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all().order_by('id')
    serializer_class = OfficeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]

class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all().order_by('id')
    serializer_class = BuildingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]

class Workplace_offViewSet(viewsets.ModelViewSet):
    queryset = Workplace_off.objects.all().order_by('id')
    serializer_class = Workplace_offSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]

class ReservedViewSet(viewsets.ModelViewSet):
    queryset = Reserved.objects.all().order_by('id')
    serializer_class = ReservedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter]
