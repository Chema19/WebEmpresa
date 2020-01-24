from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length= 200, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name="categoría"
        verbose_name_plural="categorias"
        ordering=["-created"]
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="titulo")
    content = models.TextField(verbose_name="contenido")
    published= models.DateTimeField(verbose_name="Fecha de publicación", default=timezone.now)