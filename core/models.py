from django.db import models

class Processo(models.Model):

    numero_processo = models.CharField(max_length=20)
    dados_processo = models.TextField()

    def __str__(self):
        return self.numero_processo

