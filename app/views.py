from django.shortcuts import render
from app import models
# Create your views here.

def HOME(requests):
    explore = models.exploreproperties.objects.all()
    photo = models.ourcommunity.objects.all()

    data = {
        'explore':explore,
        "ourcommunity":photo,
    }

    return render(requests,'index.html')


def CONTACT(requests):
    return render(requests,'index.html')


def GALLERY(requests):
    return render(requests,'index.html')


def ABOUT(requests):
    return render(requests,'index.html')


def PACKAGE(requests):
    return render(requests,'index.html')


def CARRER(requests):
    return render(requests,'index.html')


def TESTIMONIAL(requests):
    return render(requests,'index.html')