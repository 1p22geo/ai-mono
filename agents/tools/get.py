from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

from typing import Optional, Type

# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
import json


class ArticleContent(BaseModel):
    title: str = Field(
        description="Title of the article")
    ready: bool = Field(
        description="Is the article ready or is it still being generated"
    )
    content: str = Field(
        description="Content of the article in Markdown."
    )


docs = []
with open("data/data.json") as f:
    temp = json.load(f)
    for doc in temp:
        ar = ArticleContent(
            content=doc['content'],
            title=doc['title'],
            ready=doc['ready']
        )
        docs.append(ar)


def get(title: str) -> ArticleContent | None:
    title = title[0].upper() + title[1:].lower()
    for doc in docs:
        if doc.title == title:
            return doc
    else:
        return None


class GetInput(BaseModel):
    title: str = Field(
        description="The title of the article to retrieve"
    )


class GetTool(BaseTool):
    name = "Get"
    description = (
        "Retrieve a single article. Returns None if no article found."
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
