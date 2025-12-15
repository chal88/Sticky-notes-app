"""Tests for views in the notes app."""
from django.test import TestCase
from django.urls import reverse
from notes.models import StickyNote


class TestNoteViews(TestCase):
    """Tests for views in the notes app."""

    def test_list_view_status_code(self):
        """Test the note list view."""
        response = self.client.get(reverse("notes:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_list.html")

    def test_create_note_view(self):
        """Test the note creation view."""
        response = self.client.post(reverse("notes:create"), {
            "title": "New Note",
            "content": "Some content",
            "pinned": False,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(StickyNote.objects.count(), 1)

    def test_update_note_view(self):
        """Test the note update view."""
        note = StickyNote.objects.create(title="Original", content="Old")

        response = self.client.post(
            reverse("notes:update", kwargs={"pk": note.pk}),
            {
                "title": "Updated",
                "content": "New content",
                "pinned": False,
            },
        )

        note.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(note.title, "Updated")

    def test_delete_note_view(self):
        """Test the note deletion view."""
        note = StickyNote.objects.create(title="To Delete", content="bye")

        response = self.client.post(
            reverse("notes:delete", kwargs={"pk": note.pk})
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(StickyNote.objects.count(), 0)
