from django.urls import path
from .views import hotels, hotel_details

urlpatterns = [
    path('', hotels, name='hotels'),
    path('<int:id>/', hotel_details, name='hotel_details'),
]