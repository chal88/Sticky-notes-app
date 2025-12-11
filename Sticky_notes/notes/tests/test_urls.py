"""Tests for URL routing in the notes app."""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from notes import views


class TestURLs(SimpleTestCase):
    """Tests for URL routing in the notes app."""

    def test_note_list_url(self):
        """Test the URL for the note list view."""
        url = reverse("notes:list")
        self.assertEqual(resolve(url).func, views.note_list)

    def test_note_create_url(self):
        """Test the URL for the note creation view."""
        url = reverse("notes:create")
        self.assertEqual(resolve(url).func, views.note_create)

    def test_note_edit_url(self):
        """Test the URL for the note edit view."""
        url = reverse("notes:edit", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func, views.note_edit)

    def test_note_delete_url(self):
        """Test the URL for the note deletion view."""
        url = reverse("notes:delete", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func, views.note_delete)
