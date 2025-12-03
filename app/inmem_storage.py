"""In-memory storage implementation for notes."""
from app.note import Note


class InMemoryStorage:
    """Simple in-memory storage. Does not persist."""

    def __init__(self):
        self.notes = {}

    def add(self, note):
        """Add a note to storage."""
        self.notes[note.id] = note

    def get(self, note_id):
        """Retrieve a note by its ID."""
        return self.notes.get(note_id)

    def list_all(self):
        """List all notes in storage."""
        return list(self.notes.values())

    def update(self, note):
        """Update an existing note."""
        self.notes[note.id] = note

    def delete(self, note_id):
        """Delete a note by its ID."""
        return self.notes.pop(note_id, None)

    def clear_all(self):
        """Clear all notes from storage."""
        self.notes = {}
