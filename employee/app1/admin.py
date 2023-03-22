from django.contrib import admin
from .models import Department, Role, Employee, Cars
# Register your models here.


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'salary', 'dept', 'phone', 'hire_date')
    list_display_links = ('first_name', 'last_name')


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',  )



admin.site.register(Department, DepartmentAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Cars)

