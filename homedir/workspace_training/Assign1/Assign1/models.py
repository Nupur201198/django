from django.db import models

class Department(models.Model):
    dept = models.CharField(max_length=50)
    college = models.CharField(max_length=10)
    
    def __str__(self):
        return self.dept

class Employee(models.Model):
    d_id = models.ForeignKey(Department,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=4)

    def __str__(self):
        return self.name

