
from .models import *
from rest_framework import serializers

class AddStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
     
        fields = ['first_name','last_name','email','id']
   