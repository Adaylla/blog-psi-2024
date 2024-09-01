from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=40)
    descricao = models.CharField(max_length=300)
    foto = models.ImageField(blank=True)

    def __str__(self):
        return self.titulo