from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_number = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=10)

    def __str__(self):
        return self.employee_name

class Inventory(models.Model):
    product_name = models.CharField(max_length=100)
    product_quantity = models.IntegerField()

    def __str__(self):
        return self.product_name

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_description = models.TextField(blank=True)
    project_status = models.CharField(max_length=20)

    def __str__(self):
        return self.project_name
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=10)

    def __str__(self):
        return self.customer_name