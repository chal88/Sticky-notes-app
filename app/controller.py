"""Controller module for managing notes and notebooks."""
from app.note import Note
from app.notebook import Notebook


class Controller:
    """Controller for note operations."""
    def __init__(self, storage, sync_service=None, reminder_service=None):
        self.storage = storage
        self.sync = sync_service
        self.reminder = reminder_service
        self.notebook = Notebook()

    def create_note(self, title, content):
        """Create a new note and store it."""
        note = Note(title=title, content=content)
        self.storage.add(note)
        self.notebook.add(note)
        return note

    def list_notes(self):
        """List all notes."""
        return self.storage.list_all()

    def get_note(self, note_id):
        """Retrieve a note by its ID."""
        return self.storage.get(note_id)

    def edit_note(self, note_id, title=None, content=None, pinned=None):
        """Edit an existing note."""
        note = self.storage.get(note_id)
        if not note:
            return None
        note.update(title, content, pinned)
        self.storage.update(note)
        return note

    def delete_note(self, note_id):
        """Delete a note by its ID."""
        self.storage.delete(note_id)
        self.notebook.remove(note_id)

    def pin_unpin(self, note_id):
        """Toggle pin status of a note."""
        note = self.storage.get(note_id)
        if not note:
            return None
        note.pinned = not note.pinned
        self.storage.update(note)
        return note

    def search_notes(self, term):
        """Search notes by title containing the term."""
        return [n for n in self.list_notes() if term.lower() in n.title.lower()]

    def sync_note(self, note_id):
        """Sync a note with the external service."""
        if not self.sync:
            return None
        note = self.get_note(note_id)
        return self.sync.sync(note)

    def remind(self, note_id, message):
        """Set a reminder for a note."""
        if not self.reminder:
            return None
        return self.reminder.schedule(note_id, message)
