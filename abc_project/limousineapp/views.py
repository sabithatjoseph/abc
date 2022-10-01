from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def bahrain(request):
    return render(request, 'bahrain.html')


def saudi(request):
    return render(request, 'saudi.html')


def gallery(request):
    return render(request, 'gallery.html')


def review(request):
    return render(request, 'review.html')


def contact(request):
    return render(request, 'contact.html')
