from django.db import models

# Create your models here.
class Employees(models.Model):
    employee_name=models.CharField(max_length=80)
    email=models.EmailField(max_length=80,unique=True)
    user_name=models.CharField(max_length=120,unique=True)
    password=models.CharField(max_length=100)
    salary=models.CharField(max_length=9)
    designation=models.CharField(max_length=50)
    dob=models.DateField(auto_now_add=False)

    def __str__(self):
        return self.employee_name


