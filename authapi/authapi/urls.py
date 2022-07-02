"""authapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapi.views import FirstView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView,TokenBlacklistView,TokenRefreshSlidingView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('check_auth',FirstView.as_view(),name='check_auth'),
    # path('get_api_token',ObtainAuthToken.as_view()),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
    path('api/token/verify',TokenRefreshView.as_view(),name='token_verify'),
    path('api/token/blacklist',TokenBlacklistView.as_view(),name='token_blacklist')
]


