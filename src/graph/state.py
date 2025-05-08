from typing import List, Dict, Any, Optional, Union
from typing_extensions import TypedDict

class FileReportState(TypedDict):
    file_id: str
    file_name: str
    content: Any
    analysis: Any

class GraphState(TypedDict):
    files: List[FileReportState]
    current_file_index: int
    file_analysis: Any
    synthesis_result: str
