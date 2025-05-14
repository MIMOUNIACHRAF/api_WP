from django.db import models

class Post(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} by {self.contenu}"  # This is a string

class Candidature(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    cv = models.URLField()
    offre_id = models.IntegerField()  # Index ou ID de l’offre depuis le frontend
    date_postulation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - Offre #{self.offre_id}"
