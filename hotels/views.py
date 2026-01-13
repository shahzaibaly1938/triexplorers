from django.shortcuts import render
from django.db.models import Q
from django.core.exceptions import FieldError
from .models import Hotel


# Create your views here.
def hotels(request):
    """List hotels and apply optional search/location/rating filters.

    Reads `search`, `city` (or `location`), and `rating` from GET params.
    """
    hotels_qs = Hotel.objects.all()

    params = request.GET
    query = params.get('search')
    city = params.get('city') or params.get('location')
    rating = params.get('rating')

    if query:
        hotels_qs = hotels_qs.filter(
            Q(hotel_name__icontains=query) |
            Q(hotel_description__icontains=query) |
            Q(location__icontains=query) |
            Q(amenities__icontains=query)
        )

    if city:
        hotels_qs = hotels_qs.filter(location__icontains=city)

    if rating:
        # Apply rating filter only if the model defines a rating field
        try:
            hotels_qs = hotels_qs.filter(rating__gte=rating)
        except FieldError:
            pass

    hotels_qs = hotels_qs.distinct()

    return render(request, 'hotels/hotels.html', {'hotels': hotels_qs})



def hotel_details(request, id):
    hotel = Hotel.objects.get(id=id)
    return render(request, 'hotels/hotel_details.html', {'hotel': hotel})