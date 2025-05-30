from django.contrib import admin
from .models import Package_type, Day, Transport, Place, Package
# Register your models here.


class Place_Admin(admin.ModelAdmin):
    list_display = ("place_name","place_about", "created_at")

class Package_Admin(admin.ModelAdmin):
    list_display = ["package_name", "total_price", "total_days"]



admin.site.register(Package, Package_Admin)
admin.site.register(Package_type)
admin.site.register(Day)
admin.site.register(Transport)
admin.site.register(Place, Place_Admin)