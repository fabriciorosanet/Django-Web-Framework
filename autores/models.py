from django.db import models

# Create your models here.

class autores(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=10)

    def __str__(self):
        return self.nome