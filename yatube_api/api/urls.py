from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .views import FollowView

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/follow/', FollowView.as_view()),


    path('v1/jwt/create/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(),
         name='token_verify'),
]
