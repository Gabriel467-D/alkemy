from django.urls import path
from . import views
from.views import(FraseListView,
                    FrasesVisiblesListView,
                    FrasesNoVisiblesListView,
                    FraseCreateView,
                    FraseUpdateView,
                    FraseDeleteView
                                        )

app_name = 'app_frases'

urlpatterns = [
        
        path('', FraseListView.as_view(), name='listar_frases'),
        path('visibles/', FrasesVisiblesListView.as_view(), name='frases_visibles'),
        path('no-visibles/', FrasesNoVisiblesListView.as_view(), name='frases_no_visibles'),
        path('crear/', views.FraseCreateView.as_view(), name='crear_frase'),
        path('editar/<int:pk>/', FraseUpdateView.as_view(), name='editar_frase'),
        path('borrar/<int:pk>/', FraseDeleteView.as_view(), name='borrar_frase'),
        path('ver_frases_autor/<int:autor_id>/', views.Frase_autor, name='ver_frases_autor'),
        path('listar_json/', views.frase_json, name='frases_json'),
       ]