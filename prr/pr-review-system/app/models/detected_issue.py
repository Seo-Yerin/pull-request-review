import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, Text, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.models.enums import ToolSource, Severity


class DetectedIssue(Base):
    __tablename__ = "detected_issues"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    analysis_report_id = Column(UUID(as_uuid=True), ForeignKey("analysis_reports.id"), nullable=False)

    tool_source = Column(Enum(ToolSource), nullable=False)
    issue_type = Column(String, nullable=False)  # e.g. "high_complexity", "hardcoded_secret"
    file_path = Column(String, nullable=False)
    line_number = Column(Integer, nullable=True)
    severity = Column(Enum(Severity), nullable=False)

    raw_message = Column(Text, nullable=True)       # original tool output message
    ai_explanation = Column(Text, nullable=True)    # human-friendly explanation from LLM
    ai_suggestion = Column(Text, nullable=True)      # suggested fix from LLM

    analysis_report = relationship("AnalysisReport", back_populates="detected_issues")
