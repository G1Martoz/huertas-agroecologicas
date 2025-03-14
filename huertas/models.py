from django.db import models
from django.contrib.auth.models import User

class Huerta(models.Model):
    TIPO_PLANTACION_CHOICES = [
        ('vegetal', 'Vegetal'),
        ('cereal', 'Cereal'),
    ]

    ESTACION_CHOICES = [
        ('primavera', 'Primavera'),
        ('verano', 'Verano'),
        ('otoño', 'Otoño'),
        ('invierno', 'Invierno'),
    ]

    VEGETALES_CHOICES = [
        ('tomate', 'Tomate'),
        ('lechuga', 'Lechuga'),
        ('zanahoria', 'Zanahoria'),
        ('pimiento', 'Pimiento'),
        ('cebolla', 'Cebolla'),
        ('papa', 'Papa'),
    ]

    CEREALES_CHOICES = [
        ('trigo', 'Trigo'),
        ('maiz', 'Maíz'),
        ('avena', 'Avena'),
        ('cebada', 'Cebada'),
        ('centeno', 'Centeno'),
    ]

    tipo_plantacion = models.CharField(max_length=10, choices=TIPO_PLANTACION_CHOICES)
    cultivo = models.CharField(
        max_length=20,
        choices=VEGETALES_CHOICES + CEREALES_CHOICES,
        help_text='Seleccione el tipo de cultivo según la plantación'
    )
    descripcion = models.TextField(blank=True, null=True)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)
    estacion_siembra = models.CharField(max_length=10, choices=ESTACION_CHOICES)
    estacion_cosecha = models.CharField(max_length=10, choices=ESTACION_CHOICES)
    imagen = models.ImageField(upload_to='huertas/', blank=True, null=True, help_text='Imagen de la huerta')

    def __str__(self):
        return f'{self.get_cultivo_display()} - {self.propietario.username}'

class Cultivo(models.Model):
    huerta = models.ForeignKey(Huerta, on_delete=models.CASCADE, related_name='cultivos')
    nombre = models.CharField(max_length=100)
    fecha_plantacion = models.DateField()
    fecha_cosecha_estimada = models.DateField()
    estado = models.CharField(max_length=50)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f'{self.nombre} en {self.huerta.nombre}'