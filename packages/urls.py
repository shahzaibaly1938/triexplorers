from django.urls import path
from .views import home, packages, package_details

urlpatterns = [
    path('', packages, name='packages'),
    path('<int:id>/', package_details, name='package_details'),
]