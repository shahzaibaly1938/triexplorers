from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'packages/home.html')


def packages(request):
    return render(request, 'packages/packages.html')


def contact(request):
    return render(request, 'packages/contact.html')

def about(request):
    return render(request, 'packages/about.html')