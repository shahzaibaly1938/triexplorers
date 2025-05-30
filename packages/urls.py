from django.urls import path
from .views import home, packages

urlpatterns = [
    path('', packages, name='packages'),
]