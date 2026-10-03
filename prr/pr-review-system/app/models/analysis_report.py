import uuid
from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base


class AnalysisReport(Base):
    __tablename__ = "analysis_reports"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    pull_request_id = Column(UUID(as_uuid=True), ForeignKey("pull_requests.id"), nullable=False)

    ai_summary = Column(Text, nullable=True)
    risk_assessment = Column(Text, nullable=True)

    security_score = Column(Float, nullable=True)
    maintainability_score = Column(Float, nullable=True)
    complexity_score = Column(Float, nullable=True)
    overall_score = Column(Float, nullable=True)

    # Raw output from Semgrep/Bandit/Radon kept for traceability/debugging
    raw_static_output = Column(JSONB, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    pull_request = relationship("PullRequest", back_populates="analysis_reports")
    detected_issues = relationship("DetectedIssue", back_populates="analysis_report", cascade="all, delete-orphan")
    review_history = relationship("ReviewHistory", back_populates="analysis_report")
