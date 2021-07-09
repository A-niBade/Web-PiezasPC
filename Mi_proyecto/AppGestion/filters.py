import django_filters

from .models import *

class ProcesadorFiltro(django_filters.FilterSet):
    class Meta:
        model = Procesador
        fields = '__all__'
        exclude = ["imagen","tipo","frecuencia","socket","arquitectura"]

class PlacaFiltro(django_filters.FilterSet):
    class Meta:
        model = Placa_madre
        fields = '__all__'
        exclude = ["imagen","tipo","memorias"]
class TarjetaFiltro(django_filters.FilterSet):
    class Meta:
        model = Tarjeta_video
        fields = '__all__'
        exclude = ["imagen","tipo","gpu","bus"]

