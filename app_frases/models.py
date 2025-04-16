from django.db import models
from app_autores.models import Autor

class Frase(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='frases')
    frase = models.TextField()
    fecha_frase = models.DateField()
    creado = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.autor.nombre}: {self.frase[:30]}"
    