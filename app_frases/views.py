from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy   
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from. models import Frase,Autor
# Create your views here.


class FraseListView(ListView):
        model = Frase
        template_name = 'app_frases/listar_frases.html'
        context_object_name = 'frases'

class FrasesVisiblesListView(ListView):
        model = Frase
        queryset = Frase.objects.filter(visible=True)
        template_name = 'app_frases/listar_frases.html'
        context_object_name = 'frases'

class FrasesNoVisiblesListView(ListView):
        model = Frase
        queryset = Frase.objects.filter(visible=False)
        template_name = 'app_frases/listar_frases.html' 
        context_object_name = 'frases'

class FraseCreateView(CreateView):
        model = Frase
        template_name = 'app_frases/crear_frase.html'
        fields = ['autor', 'frase', 'visible', 'fecha_frase']  
        success_url = reverse_lazy('app_frases:listar_frases')  

class FraseUpdateView(UpdateView):
        model = Frase
        template_name = 'app_frases/crear_frase.html'
        fields = ['autor', 'frase', 'visible', 'fecha_frase']  
        success_url = reverse_lazy('app_autores:listar_frases')

class FraseDeleteView(DeleteView):
        model = Frase
        template_name = 'app_frases/borrar_frase.html'
        success_url = reverse_lazy('app_frases:listar_frases')

def Frase_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    frases = autor.frases.all()
    return render(request, 'app_frases/ver_frases.html', {
        'autor': autor,
        'frases': frases
    })