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


def create(title: str) -> ArticleContent | None:
    print(f"CREATE {title}")
    q = urllib.parse.quote_plus(title)
    req = requests.get(f"http://0.0.0.0:3000/api/page/{q}")
    res = req.json()
    try:
        return ArticleContent(
            title=res['title'],
            ready=res['ready'],
            content=res['content'],
        )
    except:
        return None


class CreateInput(BaseModel):
    title: str = Field(
        description="The title of the article to create or retrieve"
    )


class CreateTool(BaseTool):
    name = "Create"
    description = (
        "Create a new article with a given title. If there already exists such an article it will be retrieved instead."
    )
    args_schema: Type[BaseModel] = CreateInput

    def _run(
        self,
        title: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> ArticleContent | None:
        """Use the tool."""
        return create(title)

    async def _arun(
        self,
        title: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> ArticleContent | None:
        """Use the tool asynchronously."""
        return create(title)
