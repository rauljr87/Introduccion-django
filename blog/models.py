from django.db import models


# Interactuar con la base de datos
# Create your models here.
# Cada vez que se hace un cambio en este archivo debemos generar una nueva migración
class Post(models.Model):
    """ Genera POST de título y contenido """

    # Declaración de campos
    title = models.CharField(max_length=250)
    # Contenido ilimitado
    content = models.TextField()

    # Style para title
    def __str__(self):
        return self.title
