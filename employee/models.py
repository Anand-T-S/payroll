from django.db import models

# Create your models here.
class Employee_list(models.Model):
    employee_name=models.CharField(max_length=80)
    email=models.EmailField(max_length=80)
    user_name=models.CharField(max_length=120)
    password=models.CharField(max_length=100)
    salary=models.CharField(max_length=9)
    designation=models.CharField(max_length=50)
    dob=models.DateField(auto_now_add=True)

