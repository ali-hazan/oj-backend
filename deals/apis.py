from .serializers import DealSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Deal
from django.utils.timezone import datetime


class DealView(generics.ListAPIView):
    queryset = Deal.objects.filter(end_date__gte=datetime.today())
    serializer_class = DealSerializer
    permission_classes = [AllowAny]