from django.contrib import admin
from .models import Status, Employee, Reporting, Department

# Register your models here.
admin.site.register(Status)
admin.site.register(Employee)
admin.site.register(Reporting)
admin.site.register(Department)