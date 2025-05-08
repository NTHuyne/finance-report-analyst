from pydantic import BaseModel, Field
from typing import Optional


class Response(BaseModel):
    """Return the response of the analysis of finance files and tables."""

    heading: Optional[str] = Field(
        None,
        description="File type, name and purpose.",
    )

    summary: Optional[str] = Field(
        None,
        description="Main findings and summary.",
    )

    analysis_detail: Optional[str] = Field(
        None,
        description="Detail of the analysis.",
    )