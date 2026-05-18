from django.shortcuts import render
from django.http import HttpResponse
from inventory.models import Equipment

# Create your views here.
def equipments_view(request):
    equipments = Equipment.objects.all()
    
    return render(request, "equipment.html", {"Equipment": equipments})

