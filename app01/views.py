from django.shortcuts import render

def lista_frutas(request):
    frutas = ['Maçã', 'Banana', 'Laranja', 'Abacaxi']
    return render(request, 'lista_frutas.html', {'frutas': frutas})

