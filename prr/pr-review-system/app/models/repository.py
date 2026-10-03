import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    github_repo_id = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False)
    full_name = Column(String, nullable=False)  # e.g. "username/repo-name"
    default_branch = Column(String, nullable=False, default="main")

    connected_at = Column(DateTime(timezone=True), server_default=func.now())

    owner = relationship("User", back_populates="repositories")
    pull_requests = relationship("PullRequest", back_populates="repository", cascade="all, delete-orphan")
