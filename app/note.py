"""Data model for a Note in the Sticky Notes application."""
from dataclasses import dataclass, field
import uuid
from datetime import datetime


@dataclass
class Note:
    """Data model for a note."""
    title: str
    content: str
    pinned: bool = False
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat())

    def update(self, title=None, content=None, pinned=None):
        """Update note attributes."""
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content
        if pinned is not None:
            self.pinned = pinned
        self.updated_at = datetime.utcnow().isoformat()

    def to_dict(self):
        """Convert Note to dictionary."""
        return self.__dict__.copy()

    @staticmethod
    def from_dict(data):
        """Create Note from dictionary."""
        return Note(
            id=data["id"],
            title=data["title"],
            content=data["content"],
            pinned=data["pinned"],
            created_at=data["created_at"],
            updated_at=data["updated_at"]
        )
