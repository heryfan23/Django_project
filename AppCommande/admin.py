from django.contrib import admin
from .models import Commande
# Register your models here.
class Donner_commande(admin.ModelAdmin):
    list_display = ("produit","id_user","adress", "Date","payement")

admin.site.register(Commande,Donner_commande)