from django.urls import path
from .views import *

urlpatterns = [
    path("insertcoms",inserer_coms,name="commente"),
]