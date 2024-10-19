from django.shortcuts import render,redirect
from lecons_django_app.models import Articles
from dotenv import load_dotenv
from AppMembres.models import Membres
from AppCommande.models import Commande
import stripe
import datetime
import os
# Create your views here.
load_dotenv()
stripe.api_key = os.environ.get("SECRET_KEY")

def pannier(request,id):
    # prix = request.session.get('prix')
    prod = Articles.objects.get(pk=id)

    if "cart" not in request.session:
        request.session['cart'] = []
        
    cart = request.session['cart']
    unique_key = int(prod.id)

    obj = {
        "id_prod": unique_key,
        "titre": prod.titre,
        "prix": prod.prix,
        "image": str(prod.images),
    }

    if obj not in cart:
        cart.append(obj)
        request.session.modified = True
    else:
        error = "Produit Tsy tafiditra"

    return redirect("http://127.0.0.1:8000/pannier/")

def supprimer_pannier(request, id):
    if 'cart' in request.session:
        cart = request.session['cart']
        for index, valeur in enumerate(cart):
            if valeur["id_prod"]== id:
                del cart[index]
                break
        request.session['cart'] = cart

    return redirect("http://127.0.0.1:8000/pannier/")

def affiche_pannier(request):
    return render(request,"pannier.html")

def procedure_payement(request):
    return render(request,"procedure.html")

def effectuer_payement(request):
    if request.method == 'POST':
        total_prix = request.POST.get("prixtotal")
        token = request.POST.get("stripeToken")
        valuecommande =  request.POST.get("commande")
        lot = request.POST.get("addresse")
        membre = Membres.objects.get(id=int(request.session["client"]["id"]))
        try:
            charge = stripe.Charge.create(
                amount=int(total_prix) * 100,
                currency="usd",
                source=token,
                description = "tester Payement avec Django"
            )
            
            commande = Commande(
                produit = valuecommande,
                id_user = membre,
                address = lot,
                payement = charge.id,
                Date = datetime.datetime.now()
            )
            commande.save()
            return render(request,"procedure.html",{"message":"Payement Réussi !"})
        except stripe.error.StripeError as e:
            error = "erreur , veuiller reésayer"
            return render(request,"procedure.html",{"error":error})
    else:
        error = "erreur , veuiller reésayer"
        return render(request,"procedure.html",{"error":error})   