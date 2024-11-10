from django.urls import path, re_path
from .views import *
from .import views




app_name = "EmployeeApp"

urlpatterns = [
    
    path('AddEmployee/',AddEmployee.as_view(),name='AddEmployee')
]