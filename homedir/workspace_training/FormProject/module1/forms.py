from django import forms

class EmployeeForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    salary = forms.DecimalField()
    