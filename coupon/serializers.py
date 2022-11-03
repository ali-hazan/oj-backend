from rest_framework import serializers
from .models import Coupon
from deals.models import Deal,Company


class CouponCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coupon
        fields = ['deal']

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ["name","city"]


class DealSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    
    class Meta:
        model = Deal
        fields = ["company","title","offer","is_percentage","city","country","start_date","end_date"]


class CouponSerializer(serializers.ModelSerializer):
    deal = DealSerializer()

    class Meta:
        model = Coupon
        fields = '__all__'