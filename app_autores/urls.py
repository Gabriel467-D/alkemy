from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views 
from.views import( AutorCreateView,AutorUpdateView
                    )

app_name = 'app_autores'

urlpatterns = [
    path('', views.presentacion, name='presentacion'),
    path('login/', LoginView.as_view(template_name='Login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='app_autores:presentacion'), name='logout'),
    path('activos/', views.lista_autores_activos, name='lista_activos'),
    path('inactivos/', views.lista_autores_inactivos, name='lista_inactivos'),
    path('listar_json/', views.lista_autores_json, name='listar_json'),
    path('todos/', views.all_autores, name='all_autores'),
    path('detalle/<int:autor_id>/', views.detalle_autor, name='detalle_autor'),
    path('borrar/<int:id>/', views.borra_autor, name='borrar_autor'),
    path('modificar_activo/<int:id>/', views.modifica_activo, name='modificar_activo'),
    path('crear/', views.AutorCreateView.as_view(), name='crear_autor'),
    path('editar/<int:pk>/', AutorUpdateView.as_view(), name='modificar_autor'),
]
        