from django.shortcuts import render

# Create your views here.

def hotels(request):
    return render(request, 'hotels/hotels.html')