from langgraph.graph import END, StateGraph, START
from src.nodes import ReportAnalysisAgent, ReportSynthesisAgent, HTMLGeneratorAgent
from src.graph.state import GraphState
from langgraph.types import Command


class MultiFileWorkflow:
    def __init__(self) -> None:
        self.workflow = StateGraph(GraphState)
        self.build_workflow_async()

    def build_workflow_async(self):
        # add nodes
        self.workflow.add_node("agent", ReportAnalysisAgent().agent_async)
        self.workflow.add_node("next_file", self.process_next_file)
        self.workflow.add_node("synthesis", ReportSynthesisAgent().agent_async)
        self.workflow.add_node("html_generator", HTMLGeneratorAgent().agent_async)

        # add edges
        self.workflow.add_edge(START, "agent")

    
    @staticmethod
    def process_next_file(state: GraphState):
        """
        Chuẩn bị file tiếp theo để phân tích và cập nhật trạng thái của file hiện tại
        """
        current_index = state.get("current_file_index", 0)
        next_index = current_index + 1
        
        # Lưu kết quả phân tích cho file hiện tại vào files
        files = state.get("files", [])
        if state["file_analysis"] and 0 <= current_index < len(files):
            analysis_result = state["file_analysis"][0] if isinstance(state["file_analysis"], list) else state["file_analysis"]
            
            files[current_index] = {
                **files[current_index],
                "analysis": analysis_result
            }
        
        # Cập nhật chỉ số file hiện tại và files đã cập nhật
        updated_state = {
            "current_file_index": next_index,
            "files": files,
        }
        
        # Nếu còn file để xử lý, chuẩn bị nội dung file
        if next_index < len(files):
            updated_state["file_analysis"] = None
            return Command(
                goto = "agent",
                update = updated_state
            )
        else:
            return Command(
                goto = "synthesis",
                update = updated_state
            )

    def compile(self):
        return self.workflow.compile()
