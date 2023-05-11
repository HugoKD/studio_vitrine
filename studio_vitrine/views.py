from django.shortcuts import render

def index(request):
    return render(request, "studio_vitrine/index.html")

def contact(request):
    return render(request, "studio_vitrine/contact.html")

def about(request):
    return render(request, "studio_vitrine/about.html")

def work(request):
    return render(request, "studio_vitrine/about.html")
