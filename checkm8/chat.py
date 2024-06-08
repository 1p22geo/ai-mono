from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models.ollama import ChatOllama
from langchain import hub
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import numpy as np
import requests
import json

import prompts


embeddings = OllamaEmbeddings(
    base_url="http://minisforum:9000", model="nomic-embed-text")

ollama = ChatOllama(
    base_url='http://minisforum:9000',
    model="llama3"
)


def ollama_json(prompt):
    res = requests.post("http://minisforum:9000/api/generate", json={
        "model": "llama3",
        "prompt": prompt,
        "format": "json",
        "stream": False
    }).json()
    return json.loads(res["response"])


def chat(history, user, settings):
    uname = user["uname"]
    system_message = prompts.CHAT_SYSTEM[settings["behavior"]]
    system = f"{system_message}\n\nThe user you are talking to is: \"{uname}\""
    messages = [
        SystemMessage(content=system)
    ]
    for message in history:
        match message["actor"]:
            case "user":
                messages.append(HumanMessage(content=message["content"]))
            case "Checkm8":
                messages.append(AIMessage(content=message["content"]))

    print(messages)
    return ollama.invoke(messages).content


def vector(text1, text2):
    a = np.array(embeddings.embed_query(text1))
    b = np.array(embeddings.embed_query(text2))

    corr = np.dot(a, b)
    a_norm = np.dot(a, a)
    b_norm = np.dot(b, b)

    corr_norm = corr**2 / a_norm / b_norm

    return corr_norm


def sentiment(content):
    sentiment_prompt = prompts.SENTIMENT
    prompt = f"{sentiment_prompt}\n```\n{content}\n```"
    return ollama_json(prompt)
