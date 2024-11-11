from .models import*
from rest_framework import serializers




class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields ="__all__"
        
class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = "__all__"