from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Employee

def index(request):
    #check for existing employees
    #display the employess in the database
    num_existing_employees = Employee.objects.order_by('id')

    template = loader.get_template('server/index.html')
    context = {
        'num_existing_employees': num_existing_employees,
    }
    return HttpResponse(template.render(context, request))
