from django.contrib.auth import get_user_model
from django.contrib.gis.db import models

User = get_user_model()


class Farmer(models.Model):
    full_name = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='farmer')

    def __str__(self):
        return f'{self.full_name}'


class Season(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.title}'


class Culture(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title}'


class Plot(models.Model):
    contour = models.PolygonField()
    farmer = models.ForeignKey('geoapp.Farmer', on_delete=models.PROTECT, related_name='plots')
    culture = models.ForeignKey('geoapp.Culture', on_delete=models.PROTECT, related_name='plots', blank=True, null=True)
    season = models.ForeignKey('geoapp.Season', on_delete=models.PROTECT, related_name='plots')

    def __str__(self):
        return f'Plot of {self.farmer}'
