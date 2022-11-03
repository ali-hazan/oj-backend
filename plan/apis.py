
from .serializers import PlanSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Plan


class PlanPublicView(generics.ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [AllowAny]