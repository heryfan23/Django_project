from django.db import models

# Create your models here.
class Articles(models.Model):
    titre = models.CharField(max_length=50)
    prix = models.IntegerField()
    desc = models.TextField()
    images = models.ImageField(upload_to="static/images")
