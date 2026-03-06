from django.db import models

class TeknoProje(models.Model):
    # 'baslik' alanını ekliyoruz
    baslik = models.CharField(max_length=200, verbose_name="Proje Başlığı") 
    detay = models.TextField(verbose_name="Proje Detayları")
    eklenme_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")
    durum = models.BooleanField(default=False, verbose_name="Tamamlandı mı?")

    def __str__(self):
        return self.baslik

    class Meta:
        verbose_name = "Büşra'nın Web Projesi"
        verbose_name_plural = "Büşra'nın Web Projeleri"