from django.db import models
from django.contrib.auth.models import User

# All models relating to Employee are created here

# Create status model
class Status(models.Model):
    name = models.CharField(max_length=20, verbose_name='Status', unique=True)
    level = models.IntegerField(default=1, verbose_name='Level')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Status'
        verbose_name = 'Status'
        db_table = 'status'

# Create department model
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Department')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Department'
        verbose_name = 'Department'
        db_table = 'department'

# Create employee model
class Employee(models.Model):

    GENDER=(
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
    )

    CURRENCY=(
        (1, 'NGN'),
        (2, 'USD'),        
    )

    # user_id = models.OneToOneField(User, on_delete=models.CASCADE, db_column='user_id')
    employee_id = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    department_id = models.ForeignKey(Department, on_delete=models.DO_NOTHING, db_column='department_id', default=1)
    job_role = models.CharField(max_length=100, blank=True, null=True)
    salary_currency = models.CharField(max_length=1, choices=CURRENCY, blank=True, null=True)    
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)
    alternative_number = models.CharField(max_length=15, blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    leave_status_id = models.ForeignKey(Status, on_delete=models.DO_NOTHING, db_column='leave_status_id', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.employee_id
    class Meta:
        verbose_name_plural = 'Employee'
        verbose_name = 'Employee'
        db_table = 'employee'

# Create reporting model
class Reporting(models.Model):
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE, db_column='employee_id', related_name='EmployeeID')
    supervisor_id = models.OneToOneField(Employee, on_delete=models.CASCADE, db_column='supervisor_id', related_name='SupervisorID')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Reporting'
        verbose_name = 'Reporting'
        db_table = 'reporting'
