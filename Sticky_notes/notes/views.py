"""Views for StickyNote model."""
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .models import StickyNote
from .forms import StickyNoteForm


class NoteListView(ListView):
    """View to list all sticky notes."""
    model = StickyNote
    context_object_name = 'notes'
    template_name = 'notes/note_list.html'
    paginate_by = 20


class NoteDetailView(DetailView):
    """View to display a single sticky note."""
    model = StickyNote
    template_name = 'notes/note_detail.html'


class NoteCreateView(CreateView):
    """View to create a new sticky note."""
    model = StickyNote
    form_class = StickyNoteForm
    template_name = 'notes/note_form.html'


class NoteUpdateView(UpdateView):
    """View to update an existing sticky note."""
    model = StickyNote
    form_class = StickyNoteForm
    template_name = 'notes/note_form.html'


class NoteDeleteView(DeleteView):
    """View to delete a sticky note."""
    model = StickyNote
    template_name = 'notes/note_confirm_delete.html'
    success_url = reverse_lazy('notes:note_list')
