"""Admin configuration for StickyNote model."""
from django.contrib import admin
from .models import StickyNote


@admin.register(StickyNote)
class StickyNoteAdmin(admin.ModelAdmin):
    """Admin view for StickyNote model."""
    list_display = ('title', 'pinned', 'updated_at')
    list_filter = ('pinned',)
    search_fields = ('title', 'content')
