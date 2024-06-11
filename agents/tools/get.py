from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

from typing import Optional, Type

# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
import requests
import urllib.parse


class ArticleContent(BaseModel):
    title: str = Field(
        description="Title of the article")
    ready: bool = Field(
        description="Is the article ready or is it still being generated"
    )
    content: str = Field(
        description="Content of the article")


def get(title: str) -> ArticleContent | None:
    print(f"GET {title}")
    q = urllib.parse.quote_plus(title)
    req = requests.get(f"http://0.0.0.0:3000/api/search?q={q}")
    res = req.json()
    for doc in res:
        return ArticleContent(
            title=doc['title'],
            ready=doc['ready'],
            content=doc['content'],
        )
    else:
        return None


class GetInput(BaseModel):
    title: str = Field(
        description="The title of the article to retrieve"
    )


class GetTool(BaseTool):
    name = "Get"
    description = (
        "Retrieve a single article with its content."
    )
    args_schema: Type[BaseModel] = GetInput

    def _run(
        self,
        title: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> ArticleContent | None:
        """Use the tool."""
        return get(title)

    async def _arun(
        self,
        title: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> ArticleContent | None:
        """Use the tool asynchronously."""
        return get(title)
