from django.apps import AppConfig


class CoreConfig(ModuleMixin, AppConfig):
    name = 'apps.core'
    verbose_name = "Cadastros"
    icon = '<<i class="material-icons">brightness_auto</i>'