from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['id']

class Provinces(models.Model):
    name = models.CharField(max_length=30, unique=True)
    surface = models.IntegerField()
    region_id = models.ForeignKey(Region, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

class Cities(models.Model):
    name = models.CharField(max_length=30)
    population = models.IntegerField()
    province_id = models.ForeignKey(Provinces, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']