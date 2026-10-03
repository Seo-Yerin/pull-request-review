import enum


class PRStatus(str, enum.Enum):
    OPEN = "open"
    CLOSED = "closed"
    MERGED = "merged"


class ToolSource(str, enum.Enum):
    SEMGREP = "semgrep"
    BANDIT = "bandit"
    RADON = "radon"


class Severity(str, enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ReviewAction(str, enum.Enum):
    ANALYZED = "analyzed"
    REVIEWED = "reviewed"
    APPROVED = "approved"
    REJECTED = "rejected"
