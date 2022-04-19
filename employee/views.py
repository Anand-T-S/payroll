from django.shortcuts import render
from employee.forms import EmployeeRegistrationForm
from django.views.generic import View
employee_list=[

]
# Create your views here.

class EmployeeCreateView(View):
    def get(self,request):
        form=EmployeeRegistrationForm()
        return render(request,"empcreate.html",{"form":form})
    def post(self,request):
        form=EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,"empcreate.html",{"form":form})
        else:
            return render(request,"empcreate.html",{"form":form})

class ListAllEmployeesView(View):
    def get(self,request):
        all_employeelist=employee_list
        return render(request,"employeelist.html",{"emplist":all_employeelist})