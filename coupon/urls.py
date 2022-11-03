from .apis import add_coupon, MyCouponView
from django.urls import path

urlpatterns = [
    path('add/', add_coupon, name='add_coupon'),
    path('my-coupons', MyCouponView.as_view(), name="my_coupon_view")
]
