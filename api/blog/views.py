from django.http import JsonResponse,HttpResponse
from .models import Post

def api_posts(request):
    posts = Post.objects.all().order_by('-date_creation')
    data = [
        {
            'titre': post.titre,
            'contenu': post.contenu,
            'date_creation': post.date_creation.strftime('%Y-%m-%d %H:%M:%S')
        }
        for post in posts
    ]
    return JsonResponse(data, safe=False)


def blog_view(request):
    return HttpResponse("This is the blog page.")

from rest_framework import generics
from .models import Candidature
from .serializers import CandidatureSerializer

class CandidatureCreateAPIView(generics.CreateAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer
