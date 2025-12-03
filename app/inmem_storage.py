"""In-memory storage implementation for notes."""
from typing import Dict, List
from .note import Note


class InMemoryStorage:
    """In-memory storage for notes."""
    def __init__(self):
        self.notes: Dict[str, Note] = {}

    def clear_all(self):
        """Remove all stored notes — used by unit tests."""
        self.notes.clear()

    def add_note(self, note: Note):
        """Store a note in memory."""
        self.notes[note.id] = note
        return note

    def list_notes(self) -> List[Note]:
        """Return all notes."""
        return list(self.notes.values())

    def get_note(self, note_id: str):
        """Retrieve a note by ID."""
        return self.notes.get(note_id)

    def delete_note(self, note_id: str):
        """Delete a note by ID. Return True if deleted."""
        if note_id in self.notes:
            del self.notes[note_id]
            return True
        return False
