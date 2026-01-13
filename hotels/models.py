from django.db import models

# Create your models here.

class Hotel_type(models.Model):
    type_name = models.CharField(max_length=100)
    additional_info = models.TextField(default='')

    def __str__(self):
        return self.type_name   
    

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_type = models.ForeignKey(Hotel_type, related_name='hotels' , on_delete=models.CASCADE)
    hotel_image = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
    hotel_image2 = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
    hotel_image3 = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
    room_standard = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
    room_deluxe = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
    room_luxuary = models.ImageField(upload_to='hotel_images/', blank=True, null=True)
    hotel_description = models.TextField()
    location = models.CharField(max_length=200)
    amenities = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hotel_name