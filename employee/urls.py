from django.urls import path
from employee import views

urlpatterns=[
    path("registration",views.EmployeeCreateView.as_view(),name="empregistration"),
    path("list",views.ListAllEmployeesView.as_view(),name="employee_list"),
    path("details/<int:id>",views.EmployeeDetailView.as_view(),name="details"),
    path("edit/<int:id>",views.EmployeeEditView.as_view(),name="editemployee"),
    path("delete/<int:id>",views.EmployeeDeleteView.as_view(),name="deleteemployee"),
    path("accounts/signup",views.SignUpView.as_view(),name="signup")
]