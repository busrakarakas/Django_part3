from django.shortcuts import render, get_object_or_404
from .models import TeknoProje

def anasayfa(request):
    projelerim = TeknoProje.objects.all()
    return render(request, "anasayfa.html", {'projeler': projelerim})

def proje_detay(request, proje_id):
    # Eğer proje bulunamazsa 404 hatası verir
    proje = get_object_or_404(TeknoProje, pk=proje_id)
    return render(request, "proje_detay.html", {'proje': proje})