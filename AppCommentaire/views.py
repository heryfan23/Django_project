from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Commentaires
# Create your views here.
def inserer_coms(request):
    if request.method == 'POST':
        id_membre = request.session['client']['id']
        id_pro = request.POST.get("id_produit")
        coms = request.POST.get("coms")
        date_coms = timezone.now().strftime('%Y-%m-%d')

        if coms != "":
            insert = Commentaires(
                id_produit = id_pro,
                id_membre = id_membre,
                commentaire = coms,
                date = str(date_coms)
            )
            insert.save()
            return redirect(f"http://127.0.0.1:8000/detail/{id_pro}",{"error":"Commentaire envoyer"})
        else:
            return redirect(f"http://127.0.0.1:8000/detail/{id_pro}",{"error":"Champs Commentaire ne doit pas vide"})