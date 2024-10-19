from django.db import models
from AppMembres.models import Membres
# Create your models here.

class Commande(models.Model):
    produit = models.TextField()
    id_user = models.ForeignKey(Membres, on_delete=models.CASCADE)
    adress = models.TextField()
    Date = models.DateField()
    payement = models.TextField()
    