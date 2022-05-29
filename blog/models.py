from django.db import models


# Interactuar con la base de datos
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    # Contenido ilimitado
    content = models.TextField()