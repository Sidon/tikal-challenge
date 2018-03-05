from django.contrib import admin
from .models import Processo

class ProcessoAdmin(admin.ModelAdmin):
    list_display = ('user', 'numero_processo', 'dados_processo',)
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ['numero_processo']

admin.site.register(Processo, ProcessoAdmin)


