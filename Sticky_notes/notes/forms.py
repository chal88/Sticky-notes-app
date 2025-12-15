"""Forms for the notes app."""
from django import forms
from .models import StickyNote  # Changed from Note to StickyNote


class StickyNoteForm(forms.ModelForm):  # Changed from NoteForm to StickyNoteForm
    """Form for creating and updating StickyNote instances."""
    class Meta:
        """Meta class for StickyNoteForm."""
        model = StickyNote  # Changed from Note to StickyNote
        fields = ['title', 'content', 'pinned']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6
            }),
            'pinned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
