from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.


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

from ferreteria.form_bulon import FerreteriaBulonesForm
from ferreteria.models import FerreteriaBulones
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
        lista_de_bulones = FerreteriaBulones.objects.all()
        contexto = {
            'formulario': formulario,
            'lista_de_bulones': lista_de_bulones
        }
        return render(request, 'ferreteria/alta-bulones.html', context=contexto)

