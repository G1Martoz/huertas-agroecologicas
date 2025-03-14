from django.db import models
from django.contrib.auth.models import User

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)
    categoria = models.CharField(max_length=100)
    destacada = models.BooleanField(default=False)

    class Meta:
        ordering = ['-fecha_publicacion']

    def __str__(self):
        return self.titulo
