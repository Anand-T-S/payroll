from django import forms
from employee.models import Employees
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields='__all__'
        widgets={
            'employee_name':forms.TextInput(attrs={'class':'form-control'}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "user_name":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "designation":forms.TextInput(attrs={"class":"form-control"}),
            "dob":forms.DateInput(attrs={"class":"form-control"}),
        }
        # fields=[
        #     "employee_name",
        #     "email",
        #     "user_name",
        #     "password",
        #     "salary",
        #     "designation",
        #     "dob"
        # ]

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        ]