from django.shortcuts import render, HttpResponse, redirect
from .models import Employee
from datetime import datetime
from django.db.models import Q

def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {'emps': emps}
    print(context)
    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        hire_date = datetime.now()
        new_emp = Employee(first_name=first_name, last_name = last_name, salary = salary, bonus = bonus, dept_id = dept, role_id = role, phone = phone, hire_date = hire_date)
        new_emp.save()
        return redirect (to='all_emp/')
    else:
        return render(request, 'add_emp.html')


def filter_emp(request, emps=None):
    if request.method == "POST":
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)
        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An exception Occurred')

def delete_emp(request, emp_id=0):
    if emp_id:
        emp_to_be_deleted = Employee.objects.get(id=emp_id)
        emp_to_be_deleted.delete()
        emps = Employee.objects.all()
        context = {
            'emps': emps
        }
        return render(request, 'all_emp.html', context)

    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'delete_emp.html',context)
