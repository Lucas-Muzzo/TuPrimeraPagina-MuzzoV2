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






