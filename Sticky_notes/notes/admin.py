"""Admin configuration for the notes app."""
from django.contrib import admin
from .models import StickyNote


@admin.register(StickyNote)
class NoteAdmin(admin.ModelAdmin):
    """Admin view for the Note model."""
    list_display = ("title", "created_at")
    search_fields = ("title", "content")
