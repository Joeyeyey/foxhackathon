from django.db import models

# Create your models here.
#Have to define a model for employees
class Employee(models.Model):
    name = models.CharField(max_length = 40)
    revenue = models.IntegerField()
