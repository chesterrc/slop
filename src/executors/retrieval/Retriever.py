from db.vectorEmbedding.IVectorEmbedding import IVectorDb
from executors.retrieval.embedding import IEmbedder


class Retriever:
    def __init__(self, vector_db: IVectorDb, embedding_client: IEmbedder):
        self._vector_db = vector_db
        self._embedding_client = embedding_client

    def embed(self, prompt: str):
        return self._embedding_client.embed(prompt)

