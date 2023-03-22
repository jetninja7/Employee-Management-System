from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path('all_emp/', views.all_emp, name="all_emp"),
    path('add_emp', views.add_emp, name='add.emp'),
    path('filter_emp', views.filter_emp, name='filter.emp'),
    path('delete_emp', views.delete_emp, name='delete_emp'),
    path('delete_emp/<int:emp_id>', views.delete_emp, name='delete_emp'),
]