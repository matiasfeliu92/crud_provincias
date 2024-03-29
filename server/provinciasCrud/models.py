from django.db import models

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['id']

class Provinces(models.Model):
    name = models.CharField(max_length=100, unique=True)
    surface = models.FloatField()
    region_id = models.ForeignKey(Region, null=True, on_delete=models.CASCADE)
    population = models.FloatField()
    density = models.FloatField()

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