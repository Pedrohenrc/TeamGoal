from django.apps import AppConfig


class SubgoalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subgoals'

    def ready(self):
        import subgoals.signals