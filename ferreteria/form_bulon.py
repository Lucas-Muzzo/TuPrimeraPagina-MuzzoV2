from django.forms import ModelForm
from ferreteria.models import FerreteriaBulones
from ferreteria.models import FerreteriaHerramientas
from ferreteria.models import FerreteriaPvc



class FerreteriaBulonesForm(ModelForm):
    class Meta:
        model=FerreteriaBulones
        fields = ['tipo_cabeza','tamaño_rosca','longitud']

class FerreteriaHerramientasForm(ModelForm):
    class Meta:
        model=FerreteriaHerramientas
        fields = ['tipo','marca']

class FerreteriaPvcForm(ModelForm):
    class Meta:
        model=FerreteriaPvc
        fields = ['accesorio','rosca']
class FerreteriaBuscaBulonForm(ModelForm):
    class Meta:
        model=FerreteriaBulones
        fields = ['tipo_cabeza',]