from django.shortcuts import render,redirect
from . models import Employee
from django.db import connection

# Create your views here.
myCursor = connection.cursor()
def empform(request):
    if request.method == "POST":
        name = request.POST['nm']
        age = request.POST['age']
        sal= request.POST['salary']
        
        # myCursor.execute("insert into app1_employee(name,age,salary) values('{}',{},{})".format(name,age,sal))

   
        e = Employee(name = name, age = age, salary = sal)
        e.save()

    return render(request,'addemp.html')

def showemp(request):
    emp = Employee.objects.all()
    return render(request,'showemp.html',{'data':emp})

def deleteemp(request,id):
    e = Employee.objects.get(id=id)
    e.delete()
    return redirect('/app1/showemp/')

def updateemp(request, id):
    e = Employee.objects.get(id = id)
    if request.method =="POST":
        nm = request.POST['nm']
        age = request.POST['age']
        sal = request.POST['salary']

        myCursor.execute("update app1_employee set name ='{}', age ={}, salary={} where id={}".format(nm,age,sal,id))
        return redirect('/app1/showemp/')
    return render(request,'updateemp.html',{'emp': e})
    