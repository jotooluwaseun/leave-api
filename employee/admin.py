from django.contrib import admin
from .models import Status, Employee, Reporting

# Register your models here.
admin.site.register(Status)
admin.site.register(Employee)
admin.site.register(Reporting)
