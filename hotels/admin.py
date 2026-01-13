from django.contrib import admin

# Register your models here.
admin.site.site_header = "TriExplorers Admin"
admin.site.site_title = "TriExplorers Admin Portal"
admin.site.index_title = "Welcome to TriExplorers Admin Portal"
from .models import Hotel, Hotel_type
admin.site.register(Hotel)
admin.site.register(Hotel_type)