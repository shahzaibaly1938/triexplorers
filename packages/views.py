from django.shortcuts import render
from .models import Package
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request, 'packages/home.html')


def packages(request):
    packages = Package.objects.all()
    # support both GET and POST filters (template currently posts form)
    data = request.POST if request.method == 'POST' else request.GET
    query = data.get('search', None)
    p_type = data.get('type', None)
    destination = data.get('destination', None)

    if p_type:
        # package_type is a FK to Package_type; match by name (case-insensitive)
        packages = packages.filter(package_type__type_name__iexact=p_type)
    if destination:
        # places is a M2M to Place; filter by place name
        packages = packages.filter(places__place_name__icontains=destination)
    if query:
        packages = packages.filter(Q(package_name__icontains=query) | Q(package_description__icontains=query))

    packages = packages.distinct()

    return render(request, 'packages/packages.html', {'packages': packages})

def package_details(request, id):
    package = Package.objects.get(id=id)
    return render(request, 'packages/package_details.html', {'package':package})


def contact(request):
    return render(request, 'packages/contact.html')

def about(request):
    return render(request, 'packages/about.html')