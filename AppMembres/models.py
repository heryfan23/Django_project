from django.db import models

# Create your models here.
class Membres(models.Model):
    nom = models.CharField(max_length=50)
    pseudo = models.CharField(max_length=50)
    prenom = models.TextField()
    email = models.CharField(max_length=100)
    password = models.TextField()
    photo = models.ImageField(upload_to="static/images/membres/")
    date_inscrit = models.DateTimeField()
    def __str__(self) :
        return self.pseudo
