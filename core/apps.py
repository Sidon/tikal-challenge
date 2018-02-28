from django.apps import AppConfig


class CoreConfig(ModuleMixin, AppConfig):
    name = 'core'
    verbose_name = "Cadastros"
    icon = '<<i class="material-icons">brightness_auto</i>'