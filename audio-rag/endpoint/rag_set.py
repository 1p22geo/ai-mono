import speech_recognition as sr
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.documents import Document
from langchain import hub
import os

retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

embeddings = OllamaEmbeddings(
    base_url="http://localhost:9000", model="nomic-embed-text")

ollama = Ollama(
    base_url='http://localhost:9000',
    model="mistral"
)

texts = []

chain = None


def reload():
    global chain
    global texts
    texts = []
    for f in os.listdir("data"):
        match f.split(".")[-1]:
            case "txt":
                loader = TextLoader("data/"+f)
                documents = loader.load()
                text_splitter = CharacterTextSplitter(
                    chunk_size=500, chunk_overlap=10)
                texts.extend(text_splitter.split_documents(documents))
            case "pdf":
                loader = PyPDFLoader("data/"+f)
                documents = loader.load()
                text_splitter = CharacterTextSplitter(
                    chunk_size=500, chunk_overlap=10)
                texts.extend(text_splitter.split_documents(documents))

    db = FAISS.from_documents(texts, embeddings)
    retriever = db.as_retriever()
    combine_documents_chain = create_stuff_documents_chain(
        ollama, retrieval_qa_chat_prompt
    )
    chain = create_retrieval_chain(retriever, combine_documents_chain)


def load(f):
    global chain
    global texts
    match f.split(".")[-1]:
        case "mp3":
            name = ".".join(f.split(".")[:-1])
            os.system(f"ffmpeg -i data/{name}.mp3 data/{name}.wav")
            os.remove(f"data/{name}.mp3")
            r = sr.Recognizer()
            file = sr.AudioFile(f"data/{name}.wav")
            with file as source:
                audio = r.record(source)
            txt = str(r.recognize_sphinx(audio))
            documents = [
                Document(page_content=txt, metadata={"source": f"data/{name}.wav"})]
            text_splitter = CharacterTextSplitter(
                chunk_size=500, chunk_overlap=10)
            texts.extend(text_splitter.split_documents(documents))
        case "wav":
            r = sr.Recognizer()
            file = sr.AudioFile("data/"+f)
            with file as source:
                audio = r.record(source)
            txt = str(r.recognize_sphinx(audio))
            documents = [
                Document(page_content=txt, metadata={"source": "data/"+f})]
            text_splitter = CharacterTextSplitter(
                chunk_size=500, chunk_overlap=10)
            texts.extend(text_splitter.split_documents(documents))
        case "txt":
            loader = TextLoader("data/"+f)
            documents = loader.load()
            text_splitter = CharacterTextSplitter(
                chunk_size=500, chunk_overlap=10)
            texts.extend(text_splitter.split_documents(documents))
        case "pdf":
            loader = PyPDFLoader("data/"+f)
            documents = loader.load()
            text_splitter = CharacterTextSplitter(
                chunk_size=500, chunk_overlap=10)
            texts.extend(text_splitter.split_documents(documents))
        case _:
            print(f, "not accepted")
            os.remove("data/"+f)

    db = FAISS.from_documents(texts, embeddings)
    retriever = db.as_retriever()
    combine_documents_chain = create_stuff_documents_chain(
        ollama, retrieval_qa_chat_prompt
    )
    chain = create_retrieval_chain(retriever, combine_documents_chain)


print("VectorStore ready!")


def query(prompt):
    return chain.invoke({"input": prompt})
