from django.urls import path
from .views import api_posts,blog_view

urlpatterns = [
    path('', api_posts, name='api_posts'),
    path('blog1/', blog_view, name='blog'),
]
