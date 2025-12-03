"""Sync service module."""


class SyncService:
    """Mock sync with external server."""

    def sync(self, note):
        """Simulate syncing a note to an external server."""
        return f"Synced note: {note.id}"
