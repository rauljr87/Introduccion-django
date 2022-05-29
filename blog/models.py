from django.db import models


# Interactuar con la base de datos
# Create your models here.
# Cada vez que se hace un cambio en este archivo debemos generar una nueva migración
class Post(models.Model):
    title = models.CharField(max_length=250)
    # Contenido ilimitado
    content = models.TextField()