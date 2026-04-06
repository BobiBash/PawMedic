from django.apps import AppConfig


class StatusConfig(AppConfig):
    name = 'notifications'

    def ready(self):
        import notifications.signals
