from django.db import models

# Create your models here.

class Tipo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return  self.nombre

class Procesador(models.Model):
    nombre = models.CharField(max_length=50)
    frecuencia = models.IntegerField()
    socket = models.CharField(max_length=50)
    nucleos = models.IntegerField()
    hilos = models.IntegerField()
    arquitectura = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="procesadores", null=True)

    def __str__(self):
        return self.nombre

class Placa_madre(models.Model):
    nombre = models.CharField(max_length=50)
    chipset = models.CharField(max_length=50)
    memorias = models.CharField(max_length=50)
    formato = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="placas_madre",null=True)

    def __str__(self):
        return self.nombre

class Tarjeta_video(models.Model):
    nombre = models.CharField(max_length=50)
    gpu = models.CharField(max_length=50)
    gb = models.IntegerField()
    bus = models.CharField(max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Tipo, on_delete=models.PROTECT)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="tarjetas_video", null=True)

    def __str__(self):
        return self.nombre
