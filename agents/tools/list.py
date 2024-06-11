from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)

from typing import Optional, Type, List

# Import things that are needed generically
from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
import requests


class Article(BaseModel):
    title: str = Field(
        description="Title of the article")
    ready: bool = Field(
        description="Is the article ready or is it still being generated"
    )


def find() -> List[Article]:
    print("LIST")
    req = requests.get("http://0.0.0.0:3000/api/search")
    res = req.json()
    docs = []
    for doc in res:
        docs.append(Article(
            title=doc['title'],
            ready=doc['ready'],
        ))
    return docs


class ListInput(BaseModel):
    pass


class ListTool(BaseTool):
    name = "List"
    description = (
        "Retrieve a list of all articles in the database"
    )
    args_schema: Type[BaseModel] = ListInput

    def _run(
        self,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> List[Article]:
        """Use the tool."""
        return find()

    async def _arun(
        self,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> List[Article]:
        """Use the tool asynchronously."""
        return find()
