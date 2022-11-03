from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CouponCreateSerializer, CouponSerializer
from deals.models import Deal
from .models import Coupon
import random
import string
from rest_framework import status
from rest_framework import generics


def random_char(y):
    return ''.join(random.choice(string.ascii_letters)
                   for x in range(y)).upper()


# Create your views here.
@api_view(['POST'])
def add_coupon(request):
    serializer = CouponCreateSerializer(data=request.data)
    if serializer.is_valid():
        try:
            deal = Deal.objects.get(id=serializer.data['deal'])
            user = request.user
            if user.available_loyality_point >= deal.points:
                coupon = Coupon()
                coupon.code = random_char(5)
                coupon.deal = deal
                coupon.requested_by = user
                coupon.expire_at = deal.end_date
                coupon.save()
                user.available_loyality_point = user.available_loyality_point - deal.points
                user.save()
            else:
                return Response(
                    {"error": {
                        "points": ["You Don't have enough points!"]
                    }},
                    status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)

    else:
        return Response({"error": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Coupon created successfully"})


class MyCouponView(generics.ListAPIView):

    serializer_class = CouponSerializer

    def get_queryset(self):
        return Coupon.objects.filter(requested_by=self.request.user)
