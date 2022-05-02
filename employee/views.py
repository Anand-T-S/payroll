from django.shortcuts import render,redirect
from employee.forms import EmployeeRegistrationForm,UserRegistrationForm,LoginForm
from django.views.generic import View
from employee.models import Employees
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class EmployeeCreateView(View):
    template_name="empcreate.html"   #common template for both get and post
    def get(self,request):
        form=EmployeeRegistrationForm()
        return render(request,self.template_name,{"form":form})
    def post(self,request):
        form=EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("employee_list")
        else:
            return render(request,self.template_name,{"form":form})

class ListAllEmployeesView(View):
    template_name="employeelist.html"
    def get(self,request):
        all_employeelist=Employees.objects.all()
        return render(request,self.template_name,{"emplist":all_employeelist})

class EmployeeDetailView(View):
    template_name="employeedetails.html"
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        emp=Employees.objects.get(id=id)
        return render(request,self.template_name,{"empdetails":emp})

class EmployeeEditView(View):
    template_name="empedit.html"
    def get_object(self,id):
        return Employees.objects.get(id=id)    #common ORM query for both get and post
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        emp=self.get_object(id)
        form=EmployeeRegistrationForm(instance=emp)
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        emp=self.get_object(id)
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

class SignUpView(View):
    template_name="register.html"
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm()
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)
        if not form.is_valid():
            return render(request,self.template_name,{"form":form})
        form.save()
        return redirect("signin")

class SignInView(View):
    template_name="login.html"
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                print("login success")
                return redirect("emp-home")
            else:
                print("login failed")
                return redirect("signin")

def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

def home(request,*args,**kwargs):
    return render(request,"home.html")


