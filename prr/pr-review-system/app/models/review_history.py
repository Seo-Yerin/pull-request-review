import uuid
from sqlalchemy import Column, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base
from app.models.enums import ReviewAction


class ReviewHistory(Base):
    __tablename__ = "review_history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pull_request_id = Column(UUID(as_uuid=True), ForeignKey("pull_requests.id"), nullable=False)
    analysis_report_id = Column(UUID(as_uuid=True), ForeignKey("analysis_reports.id"), nullable=True)
    reviewed_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    action = Column(Enum(ReviewAction), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    pull_request = relationship("PullRequest", back_populates="review_history")
    analysis_report = relationship("AnalysisReport", back_populates="review_history")
    reviewer = relationship("User", back_populates="review_actions")
