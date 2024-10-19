from django.shortcuts import render
from .models import Membres
import hashlib
from datetime import datetime
import os
# Create your views here.
def inscription(request):
    return render(request,"inscription.html")
def Entrer_image(request,im):
    if "photos" in request.FILES:
        fichiers = request.FILES["photos"]
        path = os.path.splitext(fichiers.name)

        new_name = f'{im}{path[1]}'
        emplacement = os.path.join("static/images/membres/", new_name)

        with open(emplacement, "wb") as destination :
            for donner in fichiers.chunks():
                destination.write(donner)
        return new_name


def mdp_crypter(x):
    hacher = hashlib.sha384()
    hacher.update(x.encode("utf-8"))

    return hacher.hexdigest()

def insertion_membre(request):
    if request.method == 'POST':
        nom = request.POST.get("nom")
        pseudo = request.POST.get("pseudo")
        prenom = request.POST.get("prenom")
        mail = request.POST.get("email")
        mdp = request.POST.get("mdp1")
        mdp2 = request.POST.get("mdp2")
        photo = request.POST.get("photos")

        if nom != "" and pseudo != "" and prenom != "" and mail != "" and mdp != "" and mdp2 != "" and photo != "":
            email_exist = Membres.objects.filter(email=mail)
            nbEmail = len(email_exist)
            if nbEmail == 0:
                if mdp == mdp2 :
                    insertion = Membres(
                        nom = nom,
                        pseudo = pseudo,
                        prenom = prenom,
                        email = mail,
                        password = mdp_crypter(mdp),
                        photo = f"static/images/membres/{Entrer_image(request,pseudo)}",
                        date_inscrit = datetime.now()
                    )
                    insertion.save()
                    # message = "Bienvenue"
                    return render(request,"message_bienvenu.html")
                    
                else:
                    erreur = "Mot de passe Non identique"
                return render(request,"inscription.html",{"diso":erreur})
            else:
                erreur = "Email deja existe"
            return render(request,"inscription.html",{"diso":erreur})
        else:
            erreur = "Tous les champs ne doient pas etre vides"
            return render(request,"inscription.html",{"diso":erreur})

    return render(request,"inscription.html")

def connection(request):
    return render(request,"connection.html")
def bienvenue(request):
    return render(request,"message_bienvenu.html")

def connection_membre(request):
    if request.method == "POST":
        teste = str(request.POST.get("emails"))
        mdp = request.POST.get("mdp_conn")
    
        validation = True
        try:
            validation = True
            emailExist = Membres.objects.get(email=teste)
            if teste != "" and mdp != "":
                if mdp_crypter(mdp) == emailExist.password:
                    validation = True
                    pass
                else:
                    validation = False
                    error = "Tous les champs ne doit pas vides"
                    return render(request,"connection.html", {"message" : error})

            if validation:
                emailExist_dict ={
                    "id": emailExist.id,
                    "nom" : emailExist.nom,
                    "pseudo" : emailExist.pseudo,
                    "prenom" : emailExist.prenom,
                    "email" : emailExist.email,
                    "photo" : str(emailExist.photo),
                    "date_inscrit" :str(emailExist.date_inscrit),
                    "pasword" : emailExist.password,
                }
                request.session["client"] = emailExist_dict
                data = emailExist_dict
                
                return render(request,"login.html", {"donner" : data})
            else:
                return render(request,"connection.html")
        except Membres.DoesNotExist:
            error = "Vous n'etes pas inscrit!!!"
            return render(request,"connection.html", {"message" : error})
        
    
    
    


def deconnecte(request):
    request.session.clear()
    return render(request,"connection.html")

def membre(request):
    data = request.session["client"]
    if len(data) !=0:
        return render(request,"membres.html", {"donner" : data})
    else:
        return render(request,"connection.html")
