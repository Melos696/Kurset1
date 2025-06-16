from django.shortcuts import render
from .models import Kurs

def lista_kurseve(request):
    kurset = Kurs.objects.all()
    return render(request, 'lista.html',{'kurset': kurset})
