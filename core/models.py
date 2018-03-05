from django.contrib.auth.models import User
from django.db import models


class Processo(models.Model):
    user = models.ForeignKey(User, related_name='user', verbose_name='Usuário')
    numero_processo = models.CharField(max_length=20, blank=False, unique=True, verbose_name='Número')
    dados_processo = models.TextField(verbose_name='Dados')

    def __str__(self):
        return self.numero_processo

    class Meta:
        verbose_name = 'Processo'
        verbose_name_plural = 'Processos'


class Logdb(models.Model):
    post_req = models.TextField(verbose_name='Post to API, via request (python)')
    post_curl = models.TextField(verbose_name='Post to API, via curl (CLI)')

    class Meta:
        verbose_name = 'Log Post'
        verbose_name_plural = 'Logs Posts'