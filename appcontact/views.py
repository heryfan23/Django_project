from django.shortcuts import render
# from .fonction import envoyer
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
def envoyer_message(request):
    if request.method == 'POST':
        nom = request.POST.get("nom")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # nom_email=[f"{email}"]
        # subject = f'Nouveau message de {nom}'
        # recipient_list = ["admin@gmail.com"]

        # envoyer(subject,message,nom_email,recipient_list)
        # print(nom_email)
        send_mail(
            nom,
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
    return render(request,"index.html",{"message": "Message envoyer"})