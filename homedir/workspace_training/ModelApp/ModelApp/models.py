from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    address = models.CharField(max_length= 40)
    
    def __str__(self):
        return self.name

class Laptop(models.Model):
    stud = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    brand = models.CharField(max_length= 20)
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.brand
