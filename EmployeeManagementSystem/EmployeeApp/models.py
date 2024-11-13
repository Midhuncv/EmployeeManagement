from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    # dynamic_fields = models.JSONField(default=dict, blank=True) 
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Password(models.Model):
    empid = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, db_column='empid')
    password = models.CharField(max_length=128) 
    confirm_password =  models.CharField(max_length=128)
    

class adminlogin(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=100, blank=True, null=True)
    adminpassword = models.CharField(max_length=150)
    # selected_fields = models.JSONField(default=dict, blank=True)


class CustomField(models.Model):
    profile = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='custom_fields')
    Phone = models.CharField(max_length=100)
    Address = models.TextField(blank=True, null=True)
    Department = models.CharField(max_length=100)
    
    
