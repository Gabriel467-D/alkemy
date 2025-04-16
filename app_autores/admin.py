from django.contrib import admin
from .models import Autor

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'fecha_nacimiento', 'fecha_fallecimiento', 'activo', 'creado', 'modificado')
    list_filter = ('activo', 'nacionalidad')
    search_fields = ('nombre',)
    ordering = ('nombre',)

admin.site.site_header = "Administrador del Proyecto Integrador"
admin.site.site_title = "Proyecto Django"
admin.site.index_title = "Bienvenido al sitio de administración"

