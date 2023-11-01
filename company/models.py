from django.db import models

from company.views import validate_phone


class Employee(models.Model):
    fullname = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    phone_number = models.CharField(
        max_length=30,
        validators=[validate_phone],
        blank=True
    )
    birth_date = models.DateField(blank=True)
    email = models.EmailField(blank=True)
    department = models.ForeignKey('Department',
                                   on_delete=models.CASCADE)


class Department(models.Model):
    department_name = models.CharField(max_length=30)
    floor = models.IntegerField()
    branch = models.ForeignKey('Branch', null=True, on_delete=models.SET_NULL)


class Branch(models.Model):
    address = models.CharField(max_length=30)
    branch_name = models.CharField(max_length=30)
