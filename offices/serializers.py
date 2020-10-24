from offices.models import Building, Office, Employee, Workplace_off, Reserved
from rest_framework.serializers import ModelSerializer


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'id', 'name', 'surname', 'img']


class BuildingSerializer(ModelSerializer):
    class Meta:
        model = Building
        fields = ['url', 'id', 'address', 'img']


class OfficeSerializer(ModelSerializer):
    class Meta:
        model = Office
        fields = ['url', 'id', 'in_which_building_is', 'office_number']


class Workplace_offSerializer(ModelSerializer):
    class Meta:
        model = Workplace_off
        fields = ['url', 'id', 'which_office', 'occupied', 'number_workplace']


class ReservedSerializer(ModelSerializer):
    class Meta:
        model = Reserved
        fields = ['url', 'id', 'place', 'who', 'start_time', 'end_time']
