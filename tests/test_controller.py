"""Unit tests for Controller."""
from app.controller import Controller
from app.inmem_storage import InMemoryStorage
from app.sync_service import SyncService
from app.reminder_service import ReminderService


def setup_controller():
    """Helper to setup a Controller with in-memory storage
    and mock services."""
    return Controller(
        storage=InMemoryStorage(),
        sync_service=SyncService(),
        reminder_service=ReminderService()
    )


def test_create_note():
    """Test creating a note."""
    c = setup_controller()
    n = c.create_note("Hello", "World")
    assert n.title == "Hello"


def test_edit_note():
    """Test editing a note."""
    c = setup_controller()
    n = c.create_note("A", "B")
    c.edit_note(n.id, title="New")
    assert c.get_note(n.id).title == "New"


def test_pin_unpin():
    """Test pinning and unpinning a note."""
    c = setup_controller()
    n = c.create_note("A", "B")
    c.pin_unpin(n.id)
    assert c.get_note(n.id).pinned is True
