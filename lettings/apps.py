from django.apps import AppConfig


class LettingsConfig(AppConfig):
    """
    Configuration class for the 'lettings' app.
    This configures the default auto field and sets the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lettings'
