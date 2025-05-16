from django.http import JsonResponse,HttpResponse
from .models import Post

def api_posts(request):
    posts = Post.objects.all().order_by('-date_creation')
    data = [
        {
            'offre_id':post.id,
            'titre': post.titre,
            'contenu': post.contenu,
            'date_creation': post.date_creation.strftime('%Y-%m-%d %H:%M:%S')
        }
        for post in posts
    ]
    return JsonResponse(data, safe=False)


def blog_view(request):
    return HttpResponse("This is the blog page.")




from rest_framework import viewsets

from rest_framework import generics
from django.core.mail import send_mail
from .models import Candidature
from .serializers import CandidatureSerializer,PostSerializer
from django.conf import settings

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_creation')
    serializer_class = PostSerializer

class CandidatureCreateAPIView(generics.CreateAPIView):
    queryset = Candidature.objects.all()
    serializer_class = CandidatureSerializer

    def perform_create(self, serializer):
        candidature = serializer.save()
        offre = Post.objects.get(id=candidature.offre.id)
        # Préparer le contenu du mail
        subject = f"Nouvelle candidature pour l'offre #{candidature.offre.id}"
        message = (
            f"Nom : {candidature.nom}\n"
            f"Email : {candidature.email}\n"
            f"CV : {candidature.cv}\n"
            f"Offre ID : {candidature.offre.id}\n"
            f"Offre titre  : {offre.titre}\n"
            f"Date de postulation : {candidature.date_postulation.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        recipient_list = ['mohammed.mimouni@gmail.com']  # Email RH

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)

