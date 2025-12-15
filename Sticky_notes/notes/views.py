"""Views for managing sticky notes."""
from django.shortcuts import render, redirect, get_object_or_404
from .models import StickyNote
from .forms import StickyNoteForm


def note_list(request):
    """View to list all sticky notes."""
    notes = StickyNote.objects.all()
    return render(request, "notes/note_list.html", {"notes": notes})


def note_create(request):
    """View to create a new sticky note."""
    if request.method == "POST":
        form = StickyNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("notes:list")
    else:
        form = StickyNoteForm()

    return render(request, "notes/note_form.html", {"form": form})


def note_detail(request, pk):
    """View to display a single sticky note."""
    note = get_object_or_404(StickyNote, pk=pk)
    return render(request, "notes/note_detail.html", {"object": note})


def note_update(request, pk):
    """View to update an existing sticky note."""
    note = get_object_or_404(StickyNote, pk=pk)

    if request.method == "POST":
        form = StickyNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes:list")
    else:
        form = StickyNoteForm(instance=note)

    return render(request, "notes/note_form.html", {"form": form})


def note_delete(request, pk):
    """View to delete a sticky note."""
    note = get_object_or_404(StickyNote, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("notes:list")

    return render(request, "notes/note_confirm_delete.html", {"object": note})
