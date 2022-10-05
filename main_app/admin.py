from django.contrib import admin

# Register your models here.
from .models import Finchcoll, Location, Season 
admin.site.register(Finchcoll)
admin.site.register(Location)
admin.site.register(Season)


