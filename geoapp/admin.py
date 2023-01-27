from django.contrib import admin

from geoapp.models import Farmer, Season, Culture

admin.site.register(Farmer)
admin.site.register(Season)
admin.site.register(Culture)
