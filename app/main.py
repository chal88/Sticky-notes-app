"""Main application logic for Sticky Notes."""
from .note import Note
from .storage import Storage

storage = Storage()


def create_note(title: str, content: str):
    """Create and store a new note."""
    note = Note.create(title, content)
    return storage.add_note(note)


def list_notes():
    """List all stored notes."""
    return storage.list_notes()


def delete_note(note_id: str):
    """Delete a note by its ID."""
    return storage.delete_note(note_id)
