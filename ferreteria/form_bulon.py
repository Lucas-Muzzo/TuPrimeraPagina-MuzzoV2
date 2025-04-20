from django.forms import ModelForm
from ferreteria.models import FerreteriaBulones


class FerreteriaBulonesForm(ModelForm):
    class Meta:
        model=FerreteriaBulones
        fields = ['tipo_cabeza','tamaño_rosca','longitud']