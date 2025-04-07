from rest_framework import serializers
from quality.models import Country, DriverInvolved, Employeesinvolved, States

class DriverInvolvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverInvolved
        fields = ['id', 'name', 'iqama_id']
        
class EmployeesinvolvedDetailSerializer(serializers.ModelSerializer):
    driver_name = DriverInvolvedSerializer(many=True)

    class Meta:
        model = Employeesinvolved
        fields = '__all__'

class EmployeesinvolvedSerializer(serializers.ModelSerializer):
    
    driver_name = serializers.PrimaryKeyRelatedField(
        queryset=DriverInvolved.objects.all(),
        many=True
    )

    class Meta:
        model = Employeesinvolved
        fields = '__all__'  # Or specify specific fields like ['title', 'author']
        
    def validate_iqama_id(self, value):
        # Check if employee_id already exists
        if self.instance:
            # If the iqama_id is not changed, allow it (no need to validate it)
            if self.instance.iqama_id == value:
                return value

        # If creating or changing the iqama_id, perform the check
        if Employeesinvolved.objects.filter(iqama_id=value).exists():
            raise serializers.ValidationError(f"Employee with this iqama_id {value} already exists.")
        
        return value
    
    
class CountrySerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Country
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
   
   
    class Meta:
        model = States
        fields = '__all__'