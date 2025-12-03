"""Unit tests for the Note class."""
from app.note import Note


def test_note_creation():
    """Create a test note"""
    note = Note("Title", "Content")
    assert note.title == "Title"
    assert note.content == "Content"


def test_note_update():
    """Update a test note"""
    note = Note("A", "B")
    note.update(title="X")
    assert note.title == "X"
