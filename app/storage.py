"""JSON file-based storage module."""
import json, os
from app.note import Note


class Storage:
    """Persistent JSON file storage."""

    def __init__(self, file_path="notes.json"):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump({}, f)

    def _load(self):
        with open(self.file_path, "r") as f:
            data = json.load(f)
        return {k: Note.from_dict(v) for k, v in data.items()}

    def _save(self, notes):
        serial = {k: v.to_dict() for k, v in notes.items()}
        with open(self.file_path, "w") as f:
            json.dump(serial, f, indent=2)

    def add(self, note):
        """Add a new note."""
        notes = self._load()
        notes[note.id] = note
        self._save(notes)

    def get(self, note_id):
        """Retrieve a note by its ID."""
        return self._load().get(note_id)

    def list_all(self):
        """List all notes."""
        return list(self._load().values())

    def update(self, note):
        """Update an existing note."""
        notes = self._load()
        notes[note.id] = note
        self._save(notes)

    def delete(self, note_id):
        """Delete a note by its ID."""
        notes = self._load()
        notes.pop(note_id, None)
        self._save(notes)

    def clear_all(self):
        """Clear all notes from storage."""
        self._save({})
