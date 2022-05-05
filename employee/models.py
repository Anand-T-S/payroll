from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employees(models.Model):
    employee_name=models.CharField(max_length=80)
    email=models.EmailField(max_length=80,unique=True)
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    password=models.CharField(max_length=100)
    salary=models.CharField(max_length=9)
    designation=models.CharField(max_length=50)
    dob=models.DateField(auto_now_add=False)

    def __str__(self):
        return self.employee_name


