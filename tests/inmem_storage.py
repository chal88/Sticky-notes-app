"""Unit tests for InMemoryStorage."""
from app.inmem_storage import InMemoryStorage
from app.note import Note


def test_inmem_add_and_get():
    """Test adding and getting a note from InMemoryStorage"""
    s = InMemoryStorage()
    n = Note("T", "C")
    s.add(n)
    assert s.get(n.id) == n
