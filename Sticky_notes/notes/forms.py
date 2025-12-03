"""Forms for StickyNote model."""
from django import forms
from .models import StickyNote


class StickyNoteForm(forms.ModelForm):
    """Form for creating and updating StickyNote instances."""
    class Meta:
        """Form options for StickyNote model."""
        model = StickyNote
        fields = ['title', 'content', 'pinned']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea
            (attrs={'class': 'form-control', 'rows': 6}),
            'pinned': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
