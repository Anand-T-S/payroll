from django.shortcuts import render
from employee.forms import EmployeeRegistrationForm
from django.views.generic import View

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
