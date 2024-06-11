from langchain_community.chat_models import ChatOllama
llm = ChatOllama(
    model="mistral",
    base_url="http://0.0.0.0:9000",
    temperature=0,
)

model = llm.bind(stop=["\nObservation"])
