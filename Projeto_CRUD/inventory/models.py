from django.db import models

# Create your models here.
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name

class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=70)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='equipment_brand')
    purchase_year = models.IntegerField(blank=True, null=True)
    warranty_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='inventory', blank=True, null=True)

    def __str__(self):
        return self.model