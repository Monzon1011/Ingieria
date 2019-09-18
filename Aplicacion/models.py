from django.db import models
# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Persona"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    Persona = models.ForeignKey(Persona)
    Producto = models.ForeignKey(Producto)
    precio = models.CharField(max_length=50)
    fecha = models.DateField()

    def __str__(self):
        return '%s compro %s' % (self.Persona, self.Producto)

    class Meta:
        verbose_name = "Compra"
        verbose_name_plural = "Compras"
