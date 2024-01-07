from django.urls import path
from .views import EmployeeList, EmployeeDetail, InventoryList, InventoryDetail, ProjectList, ProjectDetail, CustomerList, CustomerDetail

urlpatterns = [
    path('employee/', EmployeeList.as_view()),
    path('employee/<int:pk>/', EmployeeDetail.as_view()),
    path('inventory/', InventoryList.as_view()),
    path('inventory/<int:pk>/', InventoryDetail.as_view()),
    path('project/', ProjectList.as_view()),
    path('project/<int:pk>/', ProjectDetail.as_view()),
    path('customer/', CustomerList.as_view()),
    path('customer/<int:pk>/', CustomerDetail.as_view()),
]