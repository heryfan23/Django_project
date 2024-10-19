from django.db import models
from AppMembres.models import Membres
from lecons_django_app.models import Articles
# Create your models here.
class Commentaires(models.Model):
    id_produit = models.IntegerField(models.ForeignKey(Articles,on_delete=models.CASCADE))
    id_membre = models.IntegerField(models.ForeignKey(Membres,on_delete=models.CASCADE))
    commentaire = models.TextField()
    date = models.DateTimeField()