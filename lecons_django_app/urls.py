from django.urls import path
from .views import *

urlpatterns =[
    
    path("",home,name="home"),
    path("detail/<int:x>",detail,name="detail"),
]