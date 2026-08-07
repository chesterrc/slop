from src.data_models.UserInfo import UserInfo
from src.db.currentSession.ICurrentSession import ICurrentSession
from src.db.vectorEmbedding.IVectorEmbedding import IVectorDb
from src.executors.retrieval.embedding import IEmbedder


class Retriever:
    def __init__(self, vector_db: IVectorDb, embedding_client: IEmbedder):
        self._vector_db = vector_db
        self._embedding_client = embedding_client

    def embed_to_db(self, prompt: str, user_profile: UserInfo):
        encoded_prompt = self._embedding_client.embed(prompt)


