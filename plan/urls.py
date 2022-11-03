from django.urls import path
from .apis import PlanPublicView

urlpatterns = [
    path('list', PlanPublicView.as_view(), name='plan_list'),
]
