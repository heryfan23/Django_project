from django.urls import path
from .views import *

urlpatterns = [
    path("envoyer",envoyer_message,name="envoyer_email")
]