from django.shortcuts import render
from rest_framework import generics

from .models import Employee, Inventory, Project, Customer
from .serializers import EmployeeSerializer, InventorySerializer, ProjectSerializer, CustomerSerializer


# Create your views here.

