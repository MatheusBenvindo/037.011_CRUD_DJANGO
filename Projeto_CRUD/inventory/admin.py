from django.contrib import admin
from inventory.models import Equipment, Brand #IMPORTAÇÃO DE MODELOS

# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    search_fields = ('brand_name',)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'purchase_year', 'warranty_year', 'value')
    search_fields = ('model',)

admin.site.register(Equipment, EquipmentAdmin) #PARAMÊTROS PARA A PAGINA DE ADMIN
admin.site.register(Brand, BrandAdmin)