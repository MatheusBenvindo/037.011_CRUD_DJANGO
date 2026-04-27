from django.db import models

# Create your models here.
class Cars(models.Model):
    id_cars = models.AutoField(primary_key=True)
    price = models.FloatField(blank=False, null=False)
    color = models.CharField(max_length=10,null=False)
    brand = models.CharField(max_length=50, null=False, blank=True)
    model = models.CharField(max_length=20, null=False, blank=True)