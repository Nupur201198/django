from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.
def form1(request):
    ef = EmployeeForm()
    return render(request,'forms.html',{'f1':ef})
