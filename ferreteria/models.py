from django.db import models

# Create your models here.
class FerreteriaBulones(models.Model):
    tipo_cabeza=models.CharField(max_length=50)
    tamaño_rosca=models.CharField(max_length=10)
    longitud=models.IntegerField()

    def __str__(self):
        return self.tipo_cabeza

class FerreteriaHerramientas(models.Model):
    tipo=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    def __str__(self):
        return self.tipo

class FerreteriaPvc(models.Model):
    accesorio=models.CharField(max_length=50)
    rosca=models.CharField(max_length=50)
    def __str__(self):
        return self.accesorio