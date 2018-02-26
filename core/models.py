from django.contrib.auth.models import User
from django.db import models


class Processo(models.Model):
    user = models.ForeignKey(User, related_name='user', verbose_name='Usuário')
    numero_processo = models.CharField(max_length=20, blank=False, verbose_name='Número do processo')
    dados_processo = models.TextField(verbose_name='Dados do processo')

    def __str__(self):
        return self.numero_processo

    class Meta:
        verbose_name = 'Processo'
        verbose_name_plural = 'Processos'


