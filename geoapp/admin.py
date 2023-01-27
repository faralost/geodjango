from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin

from geoapp.models import Farmer, Season, Culture, Plot


class PlotAdmin(LeafletGeoAdmin):
    list_display = ('id', 'farmer', 'season', 'culture',)
    list_filter = ('farmer', 'culture', 'season',)
    search_fields = ('farmer', 'culture', 'season',)
    list_display_links = ('id', 'farmer',)


class PlotInline(LeafletGeoAdminMixin, admin.StackedInline):
    model = Plot
    extra = 0


class FarmerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name',)
    search_fields = ('full_name',)
    list_display_links = ('id', 'full_name',)
    inlines = [PlotInline, ]


admin.site.register(Farmer, FarmerAdmin)
admin.site.register(Season)
admin.site.register(Culture)
admin.site.register(Plot, PlotAdmin)
