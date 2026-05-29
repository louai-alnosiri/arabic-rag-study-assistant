from langchain_chroma import Chroma
from src.embeddings import embedding_model


DB_PATH = "data/chroma"


def create_vector_store(chunks):

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=DB_PATH
    )

    return vector_store


def load_vector_store():

    vector_store = Chroma(
        persist_directory=DB_PATH,
        embedding_function=embedding_model
    )

    return vector_store