"""doctustech URL Configuration

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

from django.urls import path
from doctustech.user.views import ActivateUserView, LoginView, UserView, PostView
from rest_framework_simplejwt.views import TokenRefreshView
from doctustech.post.views import PostView


urlpatterns = [
    path('', UserView.as_view(), name='user'),
    path('<int:id>/', UserView.as_view(), name='user'),
    path('<int:id>/posts/', PostView.as_view(), name='posts'),
    path('activate/', ActivateUserView.as_view(), name="activate"),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


