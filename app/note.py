"""Data model for a note in the Sticky Notes app."""
import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Note:
    """A simple note data model."""
    id: str
    title: str
    content: str
    created_at: str = field(default_factory=lambda:
                            datetime.utcnow().isoformat())

    @staticmethod
    def create(title: str, content: str):
        """Factory method used by tests."""
        return Note(
            id=str(uuid.uuid4()),
            title=title,
            content=content
        )

    def update(self, title=None, content=None):
        """Update the note's title and/or content."""
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content
