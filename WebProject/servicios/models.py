from django.db import models


# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios') #crea la carpeta servicios en media
    created = models.DateTimeField(auto_now_add=True) #agrega fecha automaticamente
    updated = models.DateTimeField(auto_now_add=True) #actualiza fecha auto

#Clase  verbose_name meta sirve para especificar el nombre que va tener
#tanto el modelo dentro de la tabla de la bbdd como el nombre que queremos
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
    
    def __str__(self):
        return self.titulo


