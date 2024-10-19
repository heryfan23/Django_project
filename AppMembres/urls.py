from django.urls import path
from .views import *

urlpatterns = [
    path("inscription/",inscription,name="inscription"),
    path("inscription",insertion_membre,name="membre_inscrit"),

    path("connection/",connection,name="connection"),
    path("login/",connection_membre,name="se_connecter"),

    path("deconnection/",deconnecte,name="deconnection"),

    path("bienvenue/",bienvenue,name="bienvenue"),
    path("",membre,name="membre")
    
]