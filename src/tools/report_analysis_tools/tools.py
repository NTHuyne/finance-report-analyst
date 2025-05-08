from langchain_community.utilities import DuckDuckGoSearchAPIWrapper
from langchain_community.tools import DuckDuckGoSearchResults

from pydantic import BaseModel, Field
from langchain.tools import tool


class SearchInput(BaseModel):
    query: str = Field(description="should be a search query")


@tool(name_or_callable="search-tool", description="A tool to search the web using DuckDuckGo.", args_schema=SearchInput)
def webSearch(query: str) -> str:
    """
    Search web for the query using DuckDuckGo.
    Args:
        query (str): The search query.
    Returns:
        str: The search result.
    """
    search = DuckDuckGoSearchResults()
    result = search.invoke(query)
    return result

