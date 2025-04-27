from django.urls import path
from django.http import HttpResponse    
from ferreteria.views import (alta_bulones,
                            mostrar_bulones,
                            alta_herramientas,
                            alta_pvc,
                            mostrar_herramienta,
                            mostrar_articulo,
                            buscar_bulones,
                            home,
                            FerreteriaBulonesCreateView,
                            FerreteriaBulonesDeleteView,
                            FerreteriaBulonesDetailView,
                            FerreteriaBulonesListView,
                            FerreteriaBulonesUpdateView,
                            UserLoginView,
                            UserRegisterView,
                            logout_view)

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
    path("ferreteria/alta-bulones", FerreteriaBulonesCreateView.as_view(), name="buloneria-create"),
    path("ferreteria/buloneria-list",FerreteriaBulonesListView.as_view(), name="buloneria-list"),
    path("bulones/<int:pk>", FerreteriaBulonesDetailView.as_view(), name="buloneria-detail"),
    path("bulones/<int:pk>/editar", FerreteriaBulonesUpdateView.as_view(), name="buloneria-update"),
    path("bulones/<int:pk>/eliminar", FerreteriaBulonesDeleteView.as_view(), name="buloneria-delete"),
    path("", UserLoginView.as_view(), name='login'),
    path('ferreteria/signup/', UserRegisterView.as_view(), name='signup'),
    path('ferreteria/login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),  


]