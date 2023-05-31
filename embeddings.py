from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS


def create_embeddings(chunks):
    """
    Create embeddings from text chunks using OpenAIEmbeddings.
    """
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    return knowledge_base
