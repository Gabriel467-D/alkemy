from django.contrib import admin
from .models import Frase
# Register your models here.
@admin.register(Frase)
class FrasesAmin(admin.ModelAdmin):
    list_display = ('autor', 'frase', 'fecha_frase', 'creado', 'visible')
    list_filter = ('visible', 'fecha_frase', 'autor')
    search_fields = ('frase', 'autor__nombre')
    fields = ('autor', 'frase', 'fecha_frase', 'visible', 'comentarios')