from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.CharField(max_length=150)
    autor = models.ForeignKey(User, on_delete=models.CASCADE) #establece relación (usuario-post) y elimina en cascada al borrar el autor.
    categorias = models.ManyToManyField(Categoria) #relacion con la tabla categoria
    imagen = models.ImageField(upload_to='blog',null=True,blank=True) # null, blank define como opcional el poner una imagen
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    
    def __str__(self):
        return self.titulo



