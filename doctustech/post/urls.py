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
from doctustech.post.views import PostView, CommentView, LikeView



urlpatterns = [
    path('', PostView.as_view(), name='create_post'),
    path('<int:id>/', PostView.as_view(), name='get_post_by_id'),
    path('<int:id>/likes/', LikeView.as_view(), name='post_likes'),
    path('<int:id>/comments/', CommentView.as_view(), name='post_comments'),
]