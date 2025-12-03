"""Unit tests for InMemoryStorage."""
import unittest
from app.inmem_storage import InMemoryStorage
from app.note import Note


class TestInMemoryStorage(unittest.TestCase):
    """Tests for InMemoryStorage class."""

    def setUp(self):
        self.storage = InMemoryStorage()
        self.storage.clear_all()

    def test_add_and_list_notes(self):
        """Test adding and listing notes."""
        note = Note.create("Test Title", "Test Content")
        self.storage.add_note(note)
        notes = self.storage.list_notes()
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0].title, "Test Title")

    def test_get_note(self):
        """Test retrieving a note by ID."""
        note = Note.create("A", "B")
        self.storage.add_note(note)
        fetched = self.storage.get_note(note.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.content, "B")

    def test_delete_note(self):
        """Test deleting a note by ID."""
        note = Note.create("Delete Me", "Content")
        self.storage.add_note(note)
        deleted = self.storage.delete_note(note.id)
        self.assertTrue(deleted)

        still_exists = self.storage.get_note(note.id)
        self.assertIsNone(still_exists)

    def test_delete_nonexistent_note(self):
        """Test deleting a note that does not exist."""
        deleted = self.storage.delete_note("fake-id")
        self.assertFalse(deleted)


if __name__ == "__main__":
    unittest.main()
