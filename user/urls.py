from django.urls import path
from .apis import CustomTokenObtainPairView, RegisterView, subscribe_plan,get_user_data

urlpatterns = [
    path('token/',
         CustomTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('subscribe/', subscribe_plan, name='subscribe_plan'),
    path('whoami/', get_user_data, name='get_user_data'),
    
]
