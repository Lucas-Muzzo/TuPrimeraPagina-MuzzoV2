from django.urls import path
from django.http import HttpResponse    
from ferreteria.views import alta_bulones,mostrar_bulones,alta_herramientas,alta_pvc,mostrar_herramienta,mostrar_articulo,buscar_bulones,home

app_name="ferreteria"

urlpatterns = [
    path('buloneria/',mostrar_bulones, name='buloneria'),
    path('herramientas/',mostrar_herramienta,name='herramientas'),
    path('accesoriospvc/',mostrar_articulo,name='accesoriospvc'),
    path('alta-bulones/',alta_bulones,name='alta-bulones'),
    path('alta-herramientas/',alta_herramientas,name='alta-herramientas'),
    path('alta-pvc/',alta_pvc,name='alta-pvc'),
    path('buscar-bulones/',buscar_bulones,name='buscar-bulones'),
    path('home/',home,name='home'),

]