"""Reminder service module."""


class ReminderService:
    """Simulates scheduling reminders for notes."""

    def schedule(self, note_id, message):
        """Schedule a reminder for a note."""
        return f"Reminder scheduled for note {note_id}: {message}"
