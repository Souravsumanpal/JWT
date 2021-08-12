from django.shortcuts import render
from rest_framework import permissions
from .models import Student
from .serializers import StudentSerializer
from rest_framework import serializers, viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]