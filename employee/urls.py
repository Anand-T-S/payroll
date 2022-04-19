from django.urls import path
from employee import views

urlpatterns=[
    path("registration",views.EmployeeCreateView.as_view(),name="empregistration"),
    path("list",views.ListAllEmployeesView.as_view(),name="employee_list")
]