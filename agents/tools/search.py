from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

from typing import Optional, Type, List

# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
import requests
import urllib.parse


class Article(BaseModel):
    title: str = Field(
        description="Title of the article")
    ready: bool = Field(
        description="Is the article ready or is it still being generated"
    )


def search(query: str) -> List[Article]:
    print(f"SEARCH {query}")
    q = urllib.parse.quote_plus(query)
    req = requests.get(f"http://0.0.0.0:3000/api/search?q={q}")
    res = req.json()
    docs = []
    for doc in res:
        docs.append(Article(
            title=doc['title'],
            ready=doc['ready'],
        ))
    return docs


class SearchInput(BaseModel):
    query: str = Field(
        description="The search query. Case-insensitive regex."
    )


class SearchTool(BaseTool):
    name = "Search"
    description = (
        "Search through articles in the database."
    )
    args_schema: Type[BaseModel] = SearchInput

    def _run(
        self,
        query: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> List[Article]:
        """Use the tool."""
        return search(query)

    async def _arun(
        self,
        query: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> List[Article]:
        """Use the tool asynchronously."""
        return search(query)
