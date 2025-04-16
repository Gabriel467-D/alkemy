from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy   
from django.views.generic import ListView, CreateView,UpdateView, DeleteView
from. models import Autor
from app_autores.models import Autor
from app_frases.models import Frase

    # Create your views here.


def presentacion(request):
        return render(request, 'app_autores/presentacion.html')

def all_autores(request):
        autores = Autor.objects.all()
        return render(request, 'app_autores/all_autores.html', {'autores': autores})

def lista_autores_activos(request):
        autores = Autor.objects.filter(activo=True)
        return render(request, 'app_autores/lista_autores.html', {
            'autores': autores,
            'titulo': 'Autores Activos'
        })

def lista_autores_inactivos(request):
        autores_inactivos = Autor.objects.filter(activo=False)
        return render(request, 'app_autores/lista_autores.html', {
            'autores': autores_inactivos,
            'titulo': 'Autores Inactivos'
            })

def lista_autores_json(request):
        autores = get_list_or_404(Autor)
        autores_json = serialize('json', autores)
        return JsonResponse(autores_json, safe=False)

def detalle_autor(request, autor_id):
        autor = get_object_or_404(Autor, id=autor_id)
        frases_del_autor = Frase.objects.filter(autor=autor)
        cantidad_frases = frases_del_autor.count()
        return render(request, 'app_autores/detalle_autor.html', {
        'autor': autor,
        'cantidad_frases': cantidad_frases
    })
def borra_autor(request, id):
        autor_a_borrar = get_object_or_404(Autor, id=id)
        autor_a_borrar.delete()
        return HttpResponseRedirect(reverse('app_autores:all_autores'))

def modifica_activo(request, id):
        autor_a_modicicar = get_object_or_404(Autor, id=id)
        autor_a_modicicar.activo = not autor_a_modicicar.activo
        autor_a_modicicar.save()
        return HttpResponseRedirect(reverse('app_autores:all_autores'))

class AutorCreateView(CreateView):
        model = Autor
        template_name = 'app_autores/crear_autor.html'
        fields = ['nombre', 'nacionalidad', 'fecha_nacimiento', 'fecha_fallecimiento']  
        success_url = reverse_lazy('app_autores:all_autores') 


class AutorUpdateView(UpdateView):
        model = Autor
        template_name = 'app_autores/crear_autor.html'
        fields = ['nombre', 'nacionalidad', 'fecha_nacimiento', 'fecha_fallecimiento']  
        success_url = reverse_lazy('app_autores:listar_frases')