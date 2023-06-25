from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render(request, "studio_vitrine/index.html")

def contact(request):
    if request.method=='POST':
        nom = request.POST.get("Name")
        objet = request.POST.get("Object")
        message = request.POST.get("Message")
        from_email = request.POST.get("Mail")

        send_mail(objet, message, from_email, ["irisfutur@gmail.com"])

        return render(request, 'studio_vitrine/contact.html', {'nom': nom})

    return render(request, "studio_vitrine/contact.html")

def about(request):
    return render(request, "studio_vitrine/about.html")

def requin(request):
    return render(request, "studio_vitrine/requin.html")

def rebook(request):
    return render(request, "studio_vitrine/rebook.html")

def moto(request):
    return render(request, "studio_vitrine/moto.html")
def bizarre_city(request):
    return render(request, "studio_vitrine/bizarre_city.html")

def uee(request):
    return render(request, "studio_vitrine/uee.html")

def sphinx(request):
    return render(request, "studio_vitrine/sphinx.html")

def ziak(request):
    return render(request, "studio_vitrine/ziak.html")

def booba_bts(request):
    return render(request, "studio_vitrine/booba.html")
