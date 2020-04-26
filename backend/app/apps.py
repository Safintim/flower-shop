from django.apps import AppConfig


class AppConfig(AppConfig):
    name = 'app'
    verbose_name = 'Доставка цветов'

    def ready(self):
        import app.signals
