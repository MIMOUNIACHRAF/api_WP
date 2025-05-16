from django.urls import path,include
from .views import api_posts,blog_view,CandidatureCreateAPIView,PostViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'offres', PostViewSet, basename='offre')
urlpatterns = [
    path('blog', api_posts, name='api_posts'),
    path('api/', include(router.urls)),
    path('blog1/', blog_view, name='blog'),
    path('candidatures/', CandidatureCreateAPIView.as_view(), name='candidature-create'),
]
