from django.db import models
from django.db.models.base import ModelBase

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    fees = models.IntegerField()

    def __str__(self):
     return self.first_name

class Employee(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    salary = models.IntegerField()
    mobile = models.IntegerField()

    def __str__(self):
     return self.fname
