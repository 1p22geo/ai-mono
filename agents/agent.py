from utils import _format_chat_history, AgentInput
from model import model

from tools import tools
from prompts import get_prompt
from langchain.agents.output_parsers import (
    ReActJsonSingleInputOutputParser,
)
from langchain.agents.format_scratchpad import format_log_to_messages
from langchain.agents import AgentExecutor


prompt = get_prompt(tools)

agent = (
    {
        "input": lambda x: x["input"],
        "agent_scratchpad": lambda x: format_log_to_messages(x["intermediate_steps"]),
        "chat_history": lambda x: _format_chat_history(x["chat_history"])
        if x.get("chat_history")
        else [],
    }
    | prompt
    | model
    | ReActJsonSingleInputOutputParser()
)


executor = AgentExecutor(agent=agent, tools=tools, verbose=False, handle_parsing_errors=True).with_types(
    input_type=AgentInput
)
