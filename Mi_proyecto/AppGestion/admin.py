from django.contrib import admin
from .models import Marca, Tipo, Procesador,Placa_madre,Tarjeta_video

# Register your models here.

admin.site.register(Marca)
admin.site.register(Tipo)
admin.site.register(Procesador)
admin.site.register(Placa_madre)
admin.site.register(Tarjeta_video)