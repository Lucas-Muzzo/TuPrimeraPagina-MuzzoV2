from django.db import models

# Create your models here.
class FerreteriaBulones(models.Model):
    tipo_cabeza=models.CharField(max_length=50)
    tamaño_rosca=models.CharField(max_length=10)
    longitud=models.IntegerField()

    def __str__(self):
        return self.tipo_cabeza