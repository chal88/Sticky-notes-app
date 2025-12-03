"""Unit tests for File Storage."""
import tempfile, os
from app.storage import Storage
from app.note import Note


def test_file_storage():
    """Test adding and getting a note from File Storage"""
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "notes.json")
        store = Storage(path)
        note = Note("A", "B")
        store.add(note)
        fetched = store.get(note.id)
        assert fetched.title == "A"
