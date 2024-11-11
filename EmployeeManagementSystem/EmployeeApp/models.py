from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Password(models.Model):
    empid = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, db_column='empid')
    password = models.CharField(max_length=128) 
    confirm_password =  models.CharField(max_length=128)
