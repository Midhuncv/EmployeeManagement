from django.shortcuts import render,redirect
from .models import*
from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework .response import Response
from django.http import JsonResponse
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken



def index(request):
    return render(request,'index.html')

def register(request):
    return render(request, 'Registration.html') 


def login(request):
    return render(request,'Login.html')

def ChangePassword(request):
    return render(request,'ChangePassword.html')


def Mainlogin(request):
    return render(request,'Mainlogin.html')

def Employeeprofile(request):
    return render(request,'EmployeeProfile.html')


class AddEmployee(APIView):
    def post(self, request):
        try:
            name = request.data.get('name')
            email = request.data.get('email')
            position = request.data.get('position')
            password = request.data.get('password')
            confirm_password = request.data.get('confirm_password')

            # Check if username or email already exists
            if Employee.objects.filter(name=name).exists():
                return JsonResponse({"error": "Username already exists. Please choose another one."}, status=status.HTTP_400_BAD_REQUEST)
            elif Employee.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already exists. Please choose another one."}, status=status.HTTP_400_BAD_REQUEST)

            # Check if password and confirm_password match
            if password != confirm_password:
                return JsonResponse({"error": "Passwords do not match."}, status=status.HTTP_400_BAD_REQUEST)

            # Create the employee
            employee_data = {
                'name': name,
                'email': email,
                'position': position,
            }
            employee_serializer = EmployeeSerializer(data=employee_data)

            if employee_serializer.is_valid():
                # Save the employee record
                employee = employee_serializer.save()

                # Save password as plain text
                password_data = {
                    'empid': employee.id,
                    'password': password,  
                    'confirm_password':confirm_password,
                }
                password_serializer = PasswordSerializer(data=password_data)

                if password_serializer.is_valid():
                    password_serializer.save()
                    return JsonResponse({"message": "Employee registered successfully!"}, status=status.HTTP_201_CREATED)
                else:
                    employee.delete()  # Delete employee if password save fails
                    return JsonResponse(password_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
        
        

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        print("Email:", email)
        print("Password:", password)

        try:
            employee = Employee.objects.get(email=email)
            print("employee:",employee)
        except Employee.DoesNotExist:
            return Response({
                'error': 'Employee not found'
            }, status=status.HTTP_404_NOT_FOUND)
        
        try:
            password_obj = Password.objects.get(empid=employee)  
        except Password.DoesNotExist:
            return Response({
                'error': 'Password not found for this employee'
            }, status=status.HTTP_404_NOT_FOUND)

        if password_obj.password == password:  
            

            refresh = RefreshToken.for_user(employee)  
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Invalid email or password'
            }, status=status.HTTP_401_UNAUTHORIZED)
            

class ProfileView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Extract both access token and refresh token from the Authorization headers
        access_token = request.headers.get('Authorization')
        refresh_token = request.headers.get('Refresh-Token')
        print(request)
        print("acess:",access_token)
        print("refresh:",refresh_token)

        if not access_token or not refresh_token:
            return Response({
                'error': 'Access token and Refresh token are required'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Remove 'Bearer ' prefix from the access token if present
            access_token = access_token.split(" ")[1]

            # Validate the access token
            token = AccessToken(access_token)

            # Retrieve the employee based on the user ID in the token
            employee = Employee.objects.get(id=token['user_id'])  # Assuming the 'user_id' is in the token

            # Return employee profile details
            return Response({
                'id': employee.id,
                'name': employee.name,
                'email': employee.email,
                'position': employee.position,
                # 'date_joined': employee.date_joined,
                'access_token': access_token,
                'refresh_token': refresh_token
            }, status=status.HTTP_200_OK)

        except (InvalidToken) as e:
            # Handle expired or invalid access token
            # return Response({
            #     'error': 'Invalid or expired access token. Please use the refresh token to get a new access token.',
            #     'detail': str(e)
            # }, status=status.HTTP_401_UNAUTHORIZED)

            try:
                # Use the refresh token to generate a new access token
                refresh = RefreshToken(refresh_token)
                new_access_token = str(refresh.access_token)

                # Optionally, return the new access token along with the refresh token
                return Response({
                    'message': 'Access token expired, but a new one has been generated.',
                    'new_access_token': new_access_token,
                    'refresh_token': refresh_token
                }, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({
                    'error': str(e)
                }, status=status.HTTP_401_UNAUTHORIZED)

        except Employee.DoesNotExist:
            return Response({
                'error': 'Employee not found'
            }, status=status.HTTP_404_NOT_FOUND)

        
        


        
        