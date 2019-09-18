from django.db import models
from django.utils import timezone
# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    telefono = models.CharField(max_length=50, verbose_name="Telefono")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=200, verbose_name="nombreProducto")
    marca = models.CharField(max_length=100, verbose_name="Marca")
    descripcion = models.TextField()
    nombre = models.ForeignKey('persona', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombreProducto


class Compra(models.Model):
    precio = models.CharField(max_length=50)
    nombreProducto = models.ForeignKey('producto', on_delete=models.CASCADE)
    nombre = models.ForeignKey('persona', on_delete=models.CASCADE)
    fechayhora = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.fechayhora = timezone.now()
        self.save()

    def __str__(self):
        return self.precio
