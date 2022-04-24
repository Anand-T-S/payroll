from django.shortcuts import render,redirect
from employee.forms import EmployeeRegistrationForm
from django.views.generic import View
from employee.models import Employees
# Create your views here.

class EmployeeCreateView(View):
    def get(self,request):
        form=EmployeeRegistrationForm()
        return render(request,"empcreate.html",{"form":form})
    def post(self,request):
        form=EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("employee_list")
        else:
            return render(request,"empcreate.html",{"form":form})

class ListAllEmployeesView(View):
    def get(self,request):
        all_employeelist=Employees.objects.all()
        return render(request,"employeelist.html",{"emplist":all_employeelist})

class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        emp=Employees.objects.get(id=id)
        return render(request,"employeedetails.html",{"empdetails":emp})

class EmployeeEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        emp=Employees.objects.get(id=id)
        form=EmployeeRegistrationForm(instance=emp)
        return render(request,"empedit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        emp=Employees.objects.get(id=id)
        form=EmployeeRegistrationForm(request.POST,instance=emp)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("employee_list")

class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        emp=Employees.objects.get(id=id)
        emp.delete()
        return redirect("employee_list")

