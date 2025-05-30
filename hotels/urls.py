from django.urls import path
from .views import hotels

urlpatterns = [
    path('', hotels, name='hotels'),
]