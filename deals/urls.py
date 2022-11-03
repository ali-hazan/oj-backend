from .apis import DealView
from django.urls import path

urlpatterns = [
    path('list/', DealView.as_view(), name='deal_view'),
]
