from rest_framework import serializers
from .models import Status, Employee, Reporting, Department

# Create serializer for the status model
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
    
    #def vali

# Create serializer for the department model
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


# Create serializer for the employee model
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ['created_on', 'updated_on']
        read_only_fields = ['user_id', 'leave_status_id']

# Create serializer for the reporting model
class ReportingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporting
        fields = '__all__'
        read_only_fields = ['employee_id', 'supervisor_id']
