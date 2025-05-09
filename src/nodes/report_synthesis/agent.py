from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from src.graph.state import GraphState
from configs.config import settings
from src.tools import webSearch
from langgraph.types import Command
from langgraph.graph import END
from src.nodes.report_synthesis.prompts import report_synthesis_instruction, report_synthesis_prompt_template


class ReportSynthesisAgent:
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

        self.tools = [webSearch]
        self.agent = create_react_agent(
            model=self.model,
            tools=self.tools,
            state_modifier=report_synthesis_prompt_template,
            version="v2",
            debug=False
        )

    async def agent_async(self, state: GraphState):
        try:
            file_to_synthesis = ""
            for file in state["files"]:
                file_analysis = file.get("analysis", None)
                if file_analysis:
                    file_to_synthesis += f"File {file['file_name']}:\nTitle: {file_analysis.heading}\nSummary: {file_analysis.summary}\nDetail_analysis: {file_analysis.analysis_detail}\n\n"

            if state["requirement"]:
                requirement = state["requirement"]
            else:
                requirement = "None"

            response = await self.agent.ainvoke(input = {"messages": [("user", report_synthesis_instruction.format(requirement=requirement, file_content=file_to_synthesis))]})
        
            return Command(
                goto="html_generator",
                update={
                    "synthesis_result": response['messages'][-1].content
                }
            )
        
        except Exception as e:
            return Command(
                goto="report_synthesis",
                update={
                    "synthesis_result": ""
                }
            )
