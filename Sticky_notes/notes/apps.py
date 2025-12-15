"""General configuration for the notes application."""
from django.apps import AppConfig


class NotesConfig(AppConfig):
    """Configuration for the notes app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notes'
