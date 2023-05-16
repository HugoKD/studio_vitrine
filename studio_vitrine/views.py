from django.shortcuts import render

def index(request):
    return render(request, "studio_vitrine/index.html")

def contact(request):
    return render(request, "studio_vitrine/contact.html")

def about(request):
    return render(request, "studio_vitrine/about.html")

def requin(request):
    return render(request, "studio_vitrine/requin.html")

def rebook(request):
    return render(request, "studio_vitrine/rebook.html")
