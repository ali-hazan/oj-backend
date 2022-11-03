from rest_framework import serializers
from .models import Deal, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class DealSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Deal
        fields = '__all__'
