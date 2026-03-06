from django.urls import path
from . import views

urlpatterns = [
    path('', views.anasayfa, name='anasayfa'),
    path('proje/<int:proje_id>/', views.proje_detay, name='proje_detay'),
]