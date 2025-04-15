from django.urls import path
from . import views
from.views import(FraseListView,
                  FrasesVisiblesListView,
                  FrasesNoVisiblesListView,
                  FraseCreateView,
                  FraseUpdateView,
                  FraseDeleteView
                                      )

app_name = 'app_autores'

urlpatterns = [
    path('', views.presentacion, name='presentacion'),
    path('activos/', views.lista_autores_activos, name='lista_activos'),
    path('inactivos/', views.lista_autores_inactivos, name='lista_inactivos'),
    path('listar_json/', views.lista_autores_json, name='listar_json'),
    path('todos/', views.all_autores, name='all_autores'),
    path('detalle/<int:autor_id>/', views.detalle_autor, name='detalle_autor'),
    path('borrar/<int:id>/', views.borra_autor, name='borrar_autor'),
    path('modificar_activo/<int:id>/', views.modifica_activo, name='modificar_activo'),
    path('frases/', FraseListView.as_view(), name='listar_frases'),
    path('frases/visibles/', FrasesVisiblesListView.as_view(), name='frases_visibles'),
    path('frases/no-visibles/', FrasesNoVisiblesListView.as_view(), name='frases_no_visibles'),
    path('frase_crear/', views.FraseCreateView.as_view(), name='crear_frase'),
    path('frase_editar/<int:pk>/', FraseUpdateView.as_view(), name='editar_frase'),
    path('frase_borrar/<int:pk>/', FraseDeleteView.as_view(), name='borar_frase'),
]
