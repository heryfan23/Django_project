from django.contrib import admin
from .models import Commentaires
# Register your models here.
class DonnerComm(admin.ModelAdmin):
    list_display = ('commentaire','date',"id_membre")

admin.site.register(Commentaires,DonnerComm)