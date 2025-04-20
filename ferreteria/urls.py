from django.urls import path
from django.http import HttpResponse    
from ferreteria.views import buloneria,herramientas,accesoriospvc,alta_bulones

app_name="ferreteria"

urlpatterns = [
    path('buloneria/',buloneria, name='buloneria'),
    path('herramientas/',herramientas,name='herramientas'),
    path('accesoriospvc/',accesoriospvc,name='accesoriospvc'),
    path('alta-bulones/',alta_bulones,name='alta-bulones'),
]