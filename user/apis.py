from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import RegisterSerializer, SubscribePlanSerializer, CustomTokenObtainPairSerializer, UserSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import AllowAny
from plan.models import Plan
from django.utils.timezone import datetime
from dateutil.relativedelta import *


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


def calculate_expire_at(duration_mode, duration):
    today = datetime.today()
    if duration_mode == 'Y':
        new_date = today + relativedelta(years=+duration)
        return new_date

    elif duration_mode == 'M':
        new_date = today + relativedelta(months=+duration)
        return new_date
    elif duration_mode == 'W':
        new_date = today + relativedelta(weeks=+duration)
        return new_date
    elif duration_mode == 'D':
        new_date = today + relativedelta(days=+duration)
        return new_date
    else:
        return today


@api_view(['POST'])
def subscribe_plan(request):
    serializer = SubscribePlanSerializer(data=request.data)
    if serializer.is_valid():
        subscribed = Plan.objects.get(id=serializer.data['subscribed'])
        user = request.user
        user.subscribed = subscribed
        user.available_loyality_point = subscribed.points
        user.subscribedAt = datetime.today()

        user.subscribedExpire = calculate_expire_at(subscribed.duration_mode,
                                                    subscribed.duration)
        user.save()
    else:
        return Response({"error": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)

    return Response({"message": "Plan subscribed successfully"})


@api_view(['GET'])
def get_user_data(request):

    serializer = UserSerializer(request.user)
    return Response({"data": serializer.data})
