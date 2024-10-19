from django.contrib import admin
from django.http import HttpRequest
from .models import Membres
# Register your models here.
class DonnerMembres(admin.ModelAdmin):
    list_display =("nom","pseudo","prenom","email","photo","date_inscrit")
    def has_add_permission(self, request):
        pass
    def has_change_permission(self, request, obj= None ) :
        pass

    def has_delete_permission(self, request: HttpRequest, obj=None):
        pass

admin.site.register(Membres,DonnerMembres)
