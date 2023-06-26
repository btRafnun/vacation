import uuid
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from rest_framework import serializers

# Create your models here.
""" class Apply(models.Model):
    vacation_id=models.IntegerField(MaxVal=4,MinVal=0)
    employee_id=models.IntegerField(MaxVal=100,MinVal=1)
    status=models.CharField(max_length=10)

    def __str__(self):
        return self.status  """



 
class Employee(models.Model):
    name=models.CharField(max_length=30)
    email_id=models.EmailField(max_length=100)
    employee_id = models.UUIDField(default=uuid.uuid4(), editable=False, unique=True, blank=True)
    description=models.TextField(max_length=100)
    hiring_date=models.DateField()
    position=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    #def save(self, *args, **kwargs):
        #if not self.slug:
           # self.slug = slugify(self.title)
     #   super(Employee, self).save(*args, **kwargs)
    



def validate_max_vacations(value):
    employee = serializers.context['request'].user  # Assuming employee is authenticated user
    current_year = timezone.now().year
    vacation_count = employee.vacations.filter(start_date__year=current_year).count()
    if vacation_count >= 4:
        raise ValidationError("Maximum 4 vacations allowed per year.")


class VacationApplication(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, default='pending')

    def __str__(self):
        return f"{self.employee.name} - {self.start_date} to {self.end_date}"
