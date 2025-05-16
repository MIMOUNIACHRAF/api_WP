from rest_framework import serializers
from .models import Candidature,Post

class CandidatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidature
        fields = '__all__'



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'titre', 'contenu', 'date_creation']
        read_only_fields = ['id', 'date_creation']
