from django.urls import path
from .views import api_posts,blog_view,CandidatureCreateAPIView

urlpatterns = [
    path('', api_posts, name='api_posts'),
    path('blog1/', blog_view, name='blog'),
    path('candidatures/', CandidatureCreateAPIView.as_view(), name='candidature-create'),
]
