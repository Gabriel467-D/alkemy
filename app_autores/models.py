from django.db import models

class Autor(models.Model):
    NACIONALIDADES_AUTORES = [
        ('ARG', 'Argentina'),
        ('BRA', 'Brasil'),
        ('BOL', 'Bolivia'),
        ('CHI', 'Chile'),
        ('URU', 'Uruguay'),
    ]

    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=3, choices=NACIONALIDADES_AUTORES)
    fecha_nacimiento = models.DateField()
    fecha_fallecimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


class Frase(models.Model):
    autor = models.ForeignKey(Autor, related_name='frases', on_delete=models.CASCADE)
    frase = models.TextField()
    comentarios = models.CharField(max_length=100, blank=True, null=True)
    fecha_frase = models.DateField()
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"Frase de {self.autor.nombre}"

    class Meta:
        verbose_name = "Frase"
        verbose_name_plural = "Frases"
