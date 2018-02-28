from django.db.models.signals import post_init
from django.contrib.auth.models import User
from django.db import models
from .track_data import *

@track_data('dados_processo')
class Processo(models.Model):
    user = models.ForeignKey(User, related_name='user', verbose_name='Usuário')
    numero_processo = models.CharField(max_length=20, blank=False, unique=True, verbose_name='Número')
    dados_processo = models.TextField(verbose_name='Dados')

    def __str__(self):
        return self.numero_processo

    class Meta:
        verbose_name = 'Processo'
        verbose_name_plural = 'Processos'


    @classmethod
    def process_save(cls, sender, instance, createed, **kwargs):
        if instance.has_changed('dados-processo'):
            # Fazer o  post
            print ('dado alterado')


class Logdb(models.Model):
    processo = models.ForeignKey(Processo,related_name='processo', verbose_name='Processo')
    data = models.DateField

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'


