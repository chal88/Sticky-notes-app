class Notebook:
    """A notebook/board containing many notes."""
    def __init__(self, name="Default Notebook"):
        self.name = name
        self.notes = {}

    def add(self, note):
        """Add a note to the notebook."""
        self.notes[note.id] = note

    def remove(self, note_id):
        """Remove a note from the notebook by its ID."""
        return self.notes.pop(note_id, None)

    def get(self, note_id):
        """Get a note by its ID."""
        return self.notes.get(note_id)

    def list_all(self):
        """List all notes in the notebook."""
        return list(self.notes.values())
