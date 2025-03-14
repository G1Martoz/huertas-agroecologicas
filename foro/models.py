from django.db import models
from django.contrib.auth.models import User

class Tema(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Respuesta(models.Model):
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE, related_name='respuestas')
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    es_solucion = models.BooleanField(default=False)

    class Meta:
        ordering = ['fecha_creacion']

    def __str__(self):
        return f'Respuesta de {self.autor.username} en {self.tema.titulo}'
