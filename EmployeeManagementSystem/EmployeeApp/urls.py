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
    path('AdminMainLogin/',views.AdminMainLogin,name="AdminMainLogin"),
    path('AdminProfile/',views.AdminProfile,name="AdminProfile"),
    
    
    
    
    
    
    
    
    # ------------------------API------------------------------
    
    
    path('AddEmployee/',AddEmployee.as_view(),name='AddEmployee'),
    path('LoginAPIView/',LoginAPIView.as_view(),name='LoginAPIView'),
    path('AdminLoginAPIView/',AdminLoginAPIView.as_view(),name='AdminLoginAPIView'),
    path('ProfileView/',ProfileView.as_view(),name="ProfileView"),
    path('ChangePasswordApi/',ChangePasswordApi.as_view(),name="ChangePasswordApi"),
    path('LogoutAPIView/', LogoutAPIView.as_view(), name='LogoutAPIView'),
    path('AdminProfileView/', AdminProfileView.as_view(), name='AdminProfileView'),
]