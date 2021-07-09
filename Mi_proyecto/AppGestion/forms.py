from django import forms
from .models import Placa_madre, Tarjeta_video, Procesador

class PlacaForm(forms.ModelForm):

    class Meta:
        model = Placa_madre
        fields  = '__all__'

class TarjetaForm(forms.ModelForm):

    class Meta:
        model = Tarjeta_video
        fields = '__all__'

class ProcesadorForm(forms.ModelForm):

    class Meta:
        model = Procesador
        fields = '__all__'

