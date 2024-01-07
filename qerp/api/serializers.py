from rest_framework import serializers
from .models import Employee, Inventory, Project, Customer

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('__all__')

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('__all__')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('__all__')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')