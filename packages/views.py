from django.shortcuts import render
from .models import Package
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request, 'packages/home.html')


def packages(request):
    packages = Package.objects.all()
    if request.method == 'POST':
        query = request.POST.get('search', None)
        type = request.POST.get('type', None)
        destination = request.POST.get('destination', None)
        if type:
            packages.filter(package_type=type)
        if destination:
            packages.filter(Q(places__icontains = destination))
        if query:
            packages.filter(Q(package_name__icontains = query) | Q(package_description__icontains = query))
        
    
    return render(request, 'packages/packages.html', {'packages':packages})

def package_details(request, id):
    package = Package.objects.get(id=id)
    return render(request, 'packages/package_details.html', {'package':package})


def contact(request):
    return render(request, 'packages/contact.html')

def about(request):
    return render(request, 'packages/about.html')