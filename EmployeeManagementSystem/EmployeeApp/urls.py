from django.urls import path, re_path
from .views import *
from .import views




app_name = "EmployeeApp"

urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('Mainlogin/',views.Mainlogin,name="Mainlogin"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('Employeeprofile/',views.Employeeprofile,name="Employeeprofile"),
    
    
    
    
    
    
    
    
    # ------------------------API------------------------------
    
    
    path('AddEmployee/',AddEmployee.as_view(),name='AddEmployee'),
    path('LoginAPIView/',LoginAPIView.as_view(),name='LoginAPIView'),
    path('ProfileView/',ProfileView.as_view(),name="ProfileView"),
]