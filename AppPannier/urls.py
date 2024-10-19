from django.urls import path
from .views import *

urlpatterns = [
    path("pannier/<int:id>",pannier,name="pannier"),
    path("pannier/",affiche_pannier,name="pannier"),
    path("suppr/<int:id>",supprimer_pannier,name="suppression"),
    path("stripe/",procedure_payement,name="stripe"),
    path("effectuer_payement/",effectuer_payement,name="effectuer_payement")

]