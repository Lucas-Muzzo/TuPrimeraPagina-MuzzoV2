from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'ferreteria/home.html') 

def buloneria(request):
    
    context = {
        "lista_de_bulones": [
            "Cabeza Hexagonal",
            "Cabeza Fresada",
            "Cabeza Cilíndrica",
        ]
    }

    return render(request, 'ferreteria/buloneria.html', context)







def herramientas(request):
   
    context = {
        "lista_de_herramientas": [
            "Martillo",
            "Destornillador Phillips",
            "Destornillador Plano",
        ]
    }
    
    return render(request, 'ferreteria/herramientas.html', context)

  


def accesoriospvc(request):
    
    context = {
        "listapvc": [
            "Codos 90º",
            "Codos 45º",
            "Unión doble roscada",
        ]
    }

    return render(request, 'ferreteria/accesoriospvc.html', context)


from ferreteria.form_bulon import FerreteriaBulonesForm  # Importa el formulario correctamente
from ferreteria.models import FerreteriaBulones    # Importa el modelo de base de datos
from django.shortcuts import render, redirect


def alta_bulones(request):
    if request.method == "GET":
        formulario = FerreteriaBulonesForm()
        lista_de_bulones = FerreteriaBulones.objects.all()  # Consulta los registros de la base de datos
        contexto = {
            'formulario': formulario,
            'lista_de_bulones': lista_de_bulones  # Incluye la lista en el contexto
        }
        return render(request, 'ferreteria/alta-bulones.html', context=contexto)
    else:
        formulario = FerreteriaBulonesForm(request.POST)
        if formulario.is_valid():
            modelo_de_la_base_de_datos = FerreteriaBulones(
                tipo_cabeza=formulario.cleaned_data['tipo_cabeza'],
                tamaño_rosca=formulario.cleaned_data['tamaño_rosca'],
                longitud=formulario.cleaned_data['longitud'],
            )
            modelo_de_la_base_de_datos.save()
            return redirect('/ferreteria/buloneria')

        # En caso de formulario inválido
       

from django.shortcuts import render
from ferreteria.models import FerreteriaBulones

def mostrar_bulones(request):
    bulones = FerreteriaBulones.objects.all()  # Recuperar todos los registros
    contexto = {
        "lista_de_bulones": bulones
    }
    return render(request, 'ferreteria/buloneria.html', context=contexto)




from ferreteria.form_bulon import FerreteriaHerramientasForm
from ferreteria.models import FerreteriaHerramientas
from django.shortcuts import render, redirect





def alta_herramientas(request):
    if request.method == "GET":
        formulario = FerreteriaHerramientasForm()
        lista_de_herramientas = FerreteriaHerramientas.objects.all()  # Consulta los registros de la base de datos
        contexto = {
            'formulario': formulario,
            'lista_de_herramientas': lista_de_herramientas  # Incluye la lista en el contexto
        }
        return render(request, 'ferreteria/alta-herramientas.html', context=contexto)
    else:
        formulario = FerreteriaHerramientasForm(request.POST)
        if formulario.is_valid():
            modelo_de_la_base_de_datos = FerreteriaHerramientas(
                tipo=formulario.cleaned_data['tipo'],
                marca=formulario.cleaned_data['marca'],
                
            )
            modelo_de_la_base_de_datos.save()
            return redirect('/ferreteria/herramientas')

        # En caso de formulario inválido
        #lista_de_herramientas = FerreteriaHerramientas.objects.all()
        #contexto = {
           # 'formulario': formulario,
           # 'lista_de_herramientas': lista_de_herramientas
       # }
       # return render(request, 'ferreteria/alta-herramientas.html', context=contexto)
    


def mostrar_herramienta(request):
    herramientas_1=FerreteriaHerramientas.objects.all()
    contexto = {
        "lista_de_herramientas": herramientas_1
    }
    return render(request, 'ferreteria/herramientas.html', context=contexto)













from ferreteria.form_bulon import FerreteriaPvcForm
from ferreteria.models import FerreteriaPvc
from django.shortcuts import render, redirect





def alta_pvc(request):
    if request.method == "GET":
        formulario = FerreteriaPvcForm()
        lista_de_articulos = FerreteriaPvc.objects.all()  # Consulta los registros de la base de datos
        contexto = {
            'formulario': formulario,
            'lista_de_articulos': lista_de_articulos  # Incluye la lista en el contexto
        }
        return render(request, 'ferreteria/alta-pvc.html', context=contexto)
    else:
        formulario = FerreteriaPvcForm(request.POST)
        if formulario.is_valid():
            modelo_de_la_base_de_datos = FerreteriaPvc(
                accesorio=formulario.cleaned_data['accesorio'],
                rosca=formulario.cleaned_data['rosca'],
                
            )
            modelo_de_la_base_de_datos.save()
            return redirect('/ferreteria/accesoriospvc')

        # En caso de formulario inválido
        lista_de_articulos = FerreteriaPvc.objects.all()
        contexto = {
            'formulario': formulario,
            'lista_de_articulos': lista_de_articulos
        }
        return render(request, 'ferreteria/alta-pvc.html', context=contexto)
    
def mostrar_articulo(request):
    articulos_1=FerreteriaPvc.objects.all()
    contexto = {
        "lista_de_articulos": articulos_1
    }
    return render(request, 'ferreteria/accesoriospvc.html', context=contexto)



from ferreteria.form_bulon import FerreteriaBuscaBulonForm
from django.shortcuts import render
from ferreteria.models import FerreteriaBulones  # Asegúrate de importar el modelo correspondiente

def buscar_bulones(request):
    if request.method == "GET":
        contexto = {"formulario": FerreteriaBuscaBulonForm()}
        return render(request, 'ferreteria/buscar-bulones.html', context=contexto)
    else:
        # Procesamos el formulario y devolvemos un resultado
        formulario = FerreteriaBuscaBulonForm(request.POST)
        contexto = {"formulario": formulario}  # Incluimos el formulario en el contexto

        if formulario.is_valid():
            tipo_cabeza = formulario.cleaned_data["tipo_cabeza"]
            # Filtramos por tipo_cabeza
            bulones = FerreteriaBulones.objects.filter(tipo_cabeza__icontains=tipo_cabeza)
            # Agregamos los resultados al contexto
            contexto["bulones"] = bulones
        else:
            # Incluimos los errores en caso de que el formulario no sea válido
            contexto["errores"] = formulario.errors

        return render(request, 'ferreteria/buscar-bulones.html', context=contexto)


#NUEVO CODIGO PARA TP FINAL

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

class FerreteriaBulonesListView(ListView):
    model = FerreteriaBulones
    template_name = 'ferreteria/buloneria-list.html'
    context_object_name = 'bulones'

class FerreteriaBulonesCreateView(CreateView):
    model = FerreteriaBulones
    fields = ['tipo_cabeza', 'tamaño_rosca', 'longitud']
    template_name = "ferreteria/buloneria-create.html"
    success_url = "/ferreteria/alta-bulones"  # or reverse_lazy(...)

class FerreteriaBulonesDetailView(DetailView):
    model = FerreteriaBulones
    template_name = "ferreteria/buloneria-detail.html"

class FerreteriaBulonesUpdateView(UpdateView):
    model = FerreteriaBulones
    fields = ['tipo_cabeza', 'tamaño_rosca', 'longitud']
    template_name = 'ferreteria/buloneria-update.html'
    success_url = "/ferreteria/alta-bulones"

from django.urls import reverse_lazy
class FerreteriaBulonesDeleteView(DeleteView):
    model = FerreteriaBulones
    template_name = "ferreteria/buloneria-delete.html"
    success_url = "/ferreteria/alta-bulones"
  

#CODIGO PARA EL LOG IN Y CREACION DE USUARIO
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('ferreteria:login')

    
    
class UserRegisterView(CreateView):
    template_name = 'ferreteria/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('ferreteria:login')


class UserLoginView(LoginView):

    template_name = 'ferreteria/login.html'
