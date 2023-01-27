from django.contrib.gis.db import models


class Farmer(models.Model):
    full_name = models.CharField(max_length=255)

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


