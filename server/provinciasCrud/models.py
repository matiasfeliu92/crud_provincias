from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['id']

class Provinces(models.Model):
    name = models.CharField(max_length=60, unique=True)
    surface = models.DecimalField(max_digits=10, decimal_places=2)
    region_id = models.ForeignKey(Region, null=True, on_delete=models.CASCADE)
    population = models.DecimalField(max_digits=10, decimal_places=2)
    density = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Cities(models.Model):
    name = models.CharField(max_length=30)
    population = models.DecimalField(max_digits=10, decimal_places=2)
    province_id = models.ForeignKey(Provinces, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']