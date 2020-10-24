from django.db import models
from django.urls import reverse


class Building(models.Model):
    address = models.CharField(max_length=75)
    img = models.ImageField(null=True)

    def __str__(self):
        return self.address


class Office(models.Model):
    in_which_building_is = models.ForeignKey(Building, on_delete=models.CASCADE)
    office_number = models.IntegerField('number')

    def __str__(self):
        return str(self.office_number)


class Employee(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    img = models.ImageField(null=True)
    def __str__(self):
        return f'{self.name}, {self.surname}'


class Workplace_off(models.Model):
    which_office = models.ForeignKey(Office, on_delete=models.CASCADE)
    occupied = models.BooleanField()
    number_workplace = models.IntegerField('number_workplace')

    def __str__(self):
        return f'{self.which_office}, {self.number_workplace}'

class Reserved(models.Model):
    place = models.ForeignKey(Workplace_off, on_delete=models.DO_NOTHING)
    who = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    start_time = models.DateField()
    end_time = models.DateField()

    def get_absolute_url(self):
        return reverse('buildings_list')



