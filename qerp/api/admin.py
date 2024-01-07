from django.contrib import admin
from .models import Employee, Inventory, Project, Customer

# Register your models here.

admin.site.register(Employee)
admin.site.register(Inventory)
admin.site.register(Project)
admin.site.register(Customer)