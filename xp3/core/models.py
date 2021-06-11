from django.db import models

# Create your models here.
# Modelo para la categoria
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name ="Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

# modelo para el vehiculo
class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True, verbose_name='Patente')
    marca = models.CharField(max_length=20, verbose_name='Marca vehiculo')
    modelo = models.CharField(max_length=20, null=True, blank=True, verbose_name='Modelo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.patente
