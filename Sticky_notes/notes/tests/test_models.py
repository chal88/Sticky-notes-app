"""Unit tests for the Note model in the Sticky Notes application."""
from django.test import TestCase
from notes.models import StickyNote


class TestNoteModel(TestCase):
    """Tests for the Note model."""

    def test_create_note(self):
        """Test creating a Note instance."""
        note = StickyNote.objects.create(
            title="Test Title",
            content="Test Content"
        )
        self.assertEqual(StickyNote.objects.count(), 1)
        self.assertEqual(note.title, "Test Title")
        self.assertEqual(note.content, "Test Content")

    def test_string_representation(self):
        """Test the string representation of a Note instance."""
        note = StickyNote.objects.create(title="Hello", content="world")
        self.assertEqual(str(note), "Hello")
