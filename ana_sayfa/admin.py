from django.contrib import admin
from .models import TeknoProje  # Modeli içe aktarıyoruz

# Admin paneli başlıklarını kişiselleştiriyoruz
admin.site.site_header = "Büşra'nın Yönetim Paneli"
admin.site.site_title = "Büşra'nın Web Projeleri"
admin.site.index_title = "Büşra'nın Web Projesi Yönetim Merkezi"

# Modeli kayıt ediyoruz
admin.site.register(TeknoProje)