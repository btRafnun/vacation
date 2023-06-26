from rest_framework import serializers
import uuid
from .models import VacationRequest
#from vacationapp.models import Apply
from vacationapp.models import Employee

from rest_framework import serializers
from .models import Employee, VacationApplication

"""class ApplySerializer(serializers.Serializer):
    vacation_id=serializers.CharField(max_length=4)
    employee_id=serializers.CharField(max_length=100)
    status=serializers.CharField(max_length=10)


    def create(self, validated_data):
        return Apply.objects.create(validated_data)
    


    def update(self, instance, validated_data):
        instance.status=validated_data.get('status', instance.status) """

"""class EmployeeSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=30)
    email_id=serializers.EmailField(max_length=100)
    employee_id=serializers.UUIDField(read_only=True)
    description=serializers.CharField(max_length=100)
    hiring_date=serializers.DateField()
    position=serializers.CharField(max_length=50)


def create(self,validated_data):
    return Employee.objects.create(validated_data) 

def update(self ,instance, validated_data):
    instance.name =validated_data.get('name',instance.name)     
    instance.email_id  =validated_data.get('email_id',instance.email_id)  
    instance.description  =validated_data.get('description',instance.description)    
    instance.hiring_date  =validated_data.get('hiring_date',instance.hiring_date)    
    instance.position =validated_data.get(' position',instance. position)   

    return instance  """   

        
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=['name','email_id','employee_id','description','hiring_date','position']
        


class VacationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vacation
        fields = '__all__'
        validators = [validate_max_vacations]


class VacationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationRequest
        fields = '__all__'



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class VacationApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationApplication
        fields = '__all__'
