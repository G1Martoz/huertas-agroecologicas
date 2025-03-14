from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ('herramientas', 'Herramientas'),
        ('semillas', 'Semillas'),
        ('fertilizantes', 'Fertilizantes'),
        ('otros', 'Otros'),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre

    @property
    def formatted_price(self):
        """Returns the price formatted with thousand separators and proper decimal places."""
        # Format: $1.234,56 (Argentine style)
        price_str = str(self.precio)
        if '.' in price_str:
            integer_part, decimal_part = price_str.split('.')
        else:
            integer_part, decimal_part = price_str, '00'

        # Add thousand separators
        integer_part = '{:,}'.format(int(integer_part)).replace(',', '.')
        
        # Ensure two decimal places
        decimal_part = decimal_part.ljust(2, '0')[:2]
        
        return f'${integer_part},{decimal_part}'