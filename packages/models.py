from django.db import models

# Create your models here.

class Package_type(models.Model):
    type_name = models.CharField(max_length=100)
    additional_info = models.TextField(default='')

    def __str__(self):
        return self.type_name


class Place(models.Model):
    place_name = models.CharField(max_length=80)
    place_image = models.ImageField(upload_to='place_images/', blank=True, null=True)
    place_image2 = models.ImageField(upload_to='place_images/', blank=True, null=True)
    place_image3 = models.ImageField(upload_to='place_images/', blank=True, null=True)
    place_about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.place_name

class Day(models.Model):
    day_name = models.CharField(max_length=100)
    day_place = models.ManyToManyField(Place)
    day_itinerary = models.TextField()
    day_image = models.ImageField(upload_to='days_images/', blank=True, null=True)
    day_image2 = models.ImageField(upload_to='days_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.day_name} - {self.day_place}'

class Transport(models.Model):
    transport_name = models.CharField(max_length=100)
    transport_image = models.ImageField(upload_to='transport_images/',blank=True, null=True)
    transport_image2 = models.ImageField(upload_to='transport_images/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transport_name



class Package(models.Model):
    package_name = models.CharField(max_length=100)
    package_type = models.ForeignKey(Package_type, related_name='packages' , on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    package_image = models.ImageField(upload_to='package_images', blank=True, null=True)
    package_image2 = models.ImageField(upload_to='package_images', blank=True, null=True)
    max_person = models.PositiveIntegerField()
    places = models.ManyToManyField(Place)
    total_days = models.PositiveIntegerField()
    days = models.ManyToManyField(Day)
    transport = models.ManyToManyField(Transport)
    additional_info = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.package_name