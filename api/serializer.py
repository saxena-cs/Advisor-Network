from rest_framework import serializers
from Advisor.models import Advisormodel

class Advisorserializer(serializers.ModelSerializer):
    class Meta:
        model = Advisormodel
        fields = ['id','name','profile_url']