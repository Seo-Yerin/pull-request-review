import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    github_id = Column(String, unique=True, nullable=False, index=True)
    username = Column(String, nullable=False)
    email = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)

    # NOTE: encrypt this at the application layer before storing (e.g. Fernet)
    github_access_token = Column(String, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    repositories = relationship("Repository", back_populates="owner", cascade="all, delete-orphan")
    review_actions = relationship("ReviewHistory", back_populates="reviewer")
