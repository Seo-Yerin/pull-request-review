import uuid
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base
from app.models.enums import PRStatus


class PullRequest(Base):
    __tablename__ = "pull_requests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    repository_id = Column(UUID(as_uuid=True), ForeignKey("repositories.id"), nullable=False)

    pr_number = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    source_branch = Column(String, nullable=False)
    target_branch = Column(String, nullable=False)

    files_changed = Column(Integer, default=0)
    lines_added = Column(Integer, default=0)
    lines_removed = Column(Integer, default=0)

    status = Column(Enum(PRStatus), default=PRStatus.OPEN, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_analyzed_at = Column(DateTime(timezone=True), nullable=True)

    repository = relationship("Repository", back_populates="pull_requests")
    analysis_reports = relationship("AnalysisReport", back_populates="pull_request", cascade="all, delete-orphan")
    review_history = relationship("ReviewHistory", back_populates="pull_request", cascade="all, delete-orphan")
