from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from src.graph.state import GraphState
from configs.config import settings
from src.tools import webSearch
from langgraph.types import Command
from src.nodes.report_analysis.prompts import report_analysis_instruction, report_analysis_prompt_template
from src.nodes.report_analysis.schemas import Response


class ReportAnalysisAgent:
    def __init__(self, **kwargs):

        self.model_name = settings.CONF["llm_params"]["model"]

        if "gpt" in self.model_name:
            self.model = ChatOpenAI(
                **settings.CONF["llm_configs"][self.model_name],
                **settings.CONF["llm_params"],
            )
        elif "gemini" in self.model_name:
            self.model = ChatGoogleGenerativeAI(
                **settings.CONF["llm_configs"][self.model_name],
                **settings.CONF["llm_params"]
            )
        else:
            self.model = ChatOpenAI(
                **settings.CONF["llm_configs"][self.model_name],
                **settings.CONF["llm_params"],
            )

        self.tools = []
        self.agent = create_react_agent(
            model=self.model,
            tools=self.tools,
            state_modifier=report_analysis_prompt_template,
            response_format=Response,
            debug=False
        )

    async def agent_async(self, state: GraphState):
        try:
            file_content = state["files"][state["current_file_index"]]["content"]
            response = await self.agent.ainvoke(input = {"messages": [("user", report_analysis_instruction.format(file_content=file_content))]})
        
            return Command(
                goto="next_file",
                update={
                    "file_analysis": [response['structured_response']],
                    "current_file_index": state["current_file_index"],
                }
            )
        except Exception as e:
            print(f"Error in agent_async: {e}")
            return {
                "file_analysis": [],
            }
