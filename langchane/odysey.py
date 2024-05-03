from langchain.chains import RetrievalQA
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.llms import Ollama
ollama = Ollama(
    base_url='http://minisforum:9000',
    model="llama3"
)

loader = WebBaseLoader(
    "https://www.gutenberg.org/files/1727/1727-h/1727-h.htm")
data = loader.load()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)

oembed = OllamaEmbeddings(
    base_url="http://minisforum:9000", model="nomic-embed-text")
vectorstore = Chroma.from_documents(documents=all_splits, embedding=oembed)

question = "Who is Neleus and who is in Neleus' family?"
docs = vectorstore.similarity_search(question)
len(docs)

qachain = RetrievalQA.from_chain_type(
    ollama, retriever=vectorstore.as_retriever())
print(qachain.invoke({"query": question}))
