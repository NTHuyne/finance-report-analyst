from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from src.graph.state import GraphState
from configs.config import settings
from src.nodes.html_generator.prompts import code_generator_instruction, code_generator_prompt_template, system_prompt
from langgraph.types import Command
from langgraph.graph import END


class HTMLGeneratorAgent:
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
        elif "claude" in self.model_name:
            self.model = ChatAnthropic(
                **settings.CONF["llm_configs"][self.model_name],
                **settings.CONF["llm_params"]
            )
        else:
            self.model = ChatOpenAI(
                **settings.CONF["llm_configs"][self.model_name],
                **settings.CONF["llm_params"],
            )

        self.agent = code_generator_prompt_template | self.model


    async def agent_async(self, state: GraphState):
        try:
            file_to_html = ""
            for file in state["files"]:
                file_analysis = file.get("analysis", None)
                if file_analysis:
                    file_to_html += f"File {file['file_name']}:\nTitle: {file_analysis.heading}\nSummary: {file_analysis.summary}\nDetail_analysis: {file_analysis.analysis_detail}\n\n"
            file_to_html = file_to_html + "\n\n" + state["synthesis_result"]

            response = await self.agent.ainvoke(input = {"messages": [("user", code_generator_instruction.format(content=file_to_html))]})
        
            return Command(
                goto=END,
                update={
                    "html_report": response.content.strip("```html").strip("```")
                }
            )
        
        except Exception as e:
            print(f"Error in agent_async: {e}")
            return Command(
                goto="html_generator",
                update={
                    "html_report": ""
                }
            )
