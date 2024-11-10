from django.shortcuts import render
from .models import*
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework .response import Response
from rest_framework import status

# Create your views here.

class AddEmployee(APIView):
    def post(self,request):
        try:
            name=request.data.get('name')
            email=request.data.get('email')
            position=request.data.get('position')
            phone_number=request.data.get('phone_number')
            date_of_birth=request.data.get('date_of_birth')
            address=request.data.get('address')
            department=request.data.get(' department')
            date_of_joining=request.data.get('date_of_joining')
            salary=request.data.get('salary')
            is_active=request.data.get('is_active')
            
            employee = {
                
                'name':name,
                'email':email,
                'position':position,
                'phone_number':phone_number,
                'date_of_birth':date_of_birth,
                'address':address,
                'department':department,
                'date_of_joining':date_of_joining,
                'salary':salary,
                'is_active':is_active
                
            }
            
            employee_serlizer =  EmployeeSerializer(data = employee)
            if employee_serlizer.is_valid():
                employee_serlizer.save()
                return Response({'message':'Employeee created sucessfully..'},status=status.HTTP_201_CREATED)
            else:
                return Response(employee_serlizer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        