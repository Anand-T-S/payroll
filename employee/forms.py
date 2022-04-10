from django import forms

class EmployeeRegistrationForm(forms.Form):
    employee_name=forms.CharField()
    email=forms.EmailField()
    user_name=forms.CharField()
    password=forms.CharField()
    salary=forms.CharField()
    designation=forms.CharField()
    dob=forms.DateField()
