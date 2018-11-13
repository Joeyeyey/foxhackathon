from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee
import csv

def index(request):
    #check for existing employees
    #display the employess in the database
    num_existing_employees = Employee.objects.order_by('id')
    list_employees = Employee.objects.all()

    template = loader.get_template('server/index.html')
    context = {
        'num_existing_employees': num_existing_employees,
        'list_employees': list_employees,
    }
    return HttpResponse(template.render(context, request))
