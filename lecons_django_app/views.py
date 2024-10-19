from django.shortcuts import render
from .models import Articles
from django.db import connection
# Create your views here.
def home(request):
    data = Articles.objects.all()
    context = {
        "listes_articles" : data
    }
    return render(request,"index.html", context)

def detail(request,x):
    prod = Articles.objects.get(pk=x)
    membre = Articles.objects.all()
    id_produit = x
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT AppCommentaire_commentaires.*, AppMembres_membres.*
            FROM AppCommentaire_commentaires
            INNER JOIN AppMembres_membres ON AppCommentaire_commentaires.id_membre = AppMembres_membres.id
            WHERE AppCommentaire_commentaires.id_produit = %s
        """, [id_produit])
        comments = cursor.fetchall()

    context ={
        "produit" : prod,
        "coms" : comments,
        "nbrcoms": len(comments),
        "membres": membre
    }
    return render(request,"detail.html",context)
