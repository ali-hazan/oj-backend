from .models import Plan, Benefit
from rest_framework import serializers


class PlanSerializer(serializers.ModelSerializer):
    duration_mode = serializers.CharField(source='get_duration_mode_display')

    class Meta:
        model = Plan
        fields = '__all__'
