from django.db import models
from django.urls import reverse


class StickyNote(models.Model):
    """Model representing a sticky note."""
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta options for StickyNote model."""
        ordering = ['-pinned', '-updated_at', '-created_at']

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this note."""
        return reverse('notes:note_detail', args=[str(self.id)])
