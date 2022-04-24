from django import forms
from employee.models import Employees

class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields=[
            "employee_name",
            "email",
            "user_name",
            "password",
            "salary",
            "designation",
            "dob"
        ]