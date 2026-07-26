
import asyncio

from src.db.vectorEmbedding.WeaviateVectorEmbedding import WeaviateVectorEmbedding
from src.executors.retrieval.Retriever import Retriever
from src.db.vectorEmbedding.IVectorEmbedding import IVectorDb
from app.embeddings.openai_client import OpenAIEmbeddingClient
from app.embeddings.base import EmbeddingClientInterface
from app.retrieval.job_match_retriever import VectorJobMatchRetriever
from qdrant_client import QdrantClient


class RetrievalComposition:
    """Owns the vectorEmbedding DB client, retrieval repository, embedding client,
    and job-match retriever — everything behind Database C."""

    def __init__(self):
        self._vector_client: QdrantClient | None = None
        self._vector_client_lock = asyncio.Lock()
        self._retrieval_repo: IVectorDb | None = None
        self._embedding_client: EmbeddingClientInterface | None = None
        self._job_match_retriever: JobMatchRetrieverInterface | None = None

    async def get_vector_client(self) -> QdrantClient:
        if self._vector_client is None:
            async with self._vector_client_lock:
                if self._vector_client is None:
                    client = QdrantClient(url=settings.QDRANT_URL)
                    await client.get_collections()  # verify connectivity
                    self._vector_client = client
        return self._vector_client

    async def get_retrieval_repository(self) -> IVectorDb:
        if self._retrieval_repo is None:
            client = await self.get_vector_client()
            self._retrieval_repo = WeaviateVectorEmbedding(client=client)
        return self._retrieval_repo

    def get_embedding_client(self) -> EmbeddingClientInterface:
        if self._embedding_client is None:
            self._embedding_client = OpenAIEmbeddingClient(api_key=settings.OPENAI_API_KEY)
        return self._embedding_client

    async def get_job_match_retriever(self) -> JobMatchRetrieverInterface:
        if self._job_match_retriever is None:
            retrieval_repo = await self.get_retrieval_repository()
            self._job_match_retriever = VectorJobMatchRetriever(
                retrieval_repo=retrieval_repo,
                embedding_client=self.get_embedding_client(),
            )
        return self._job_match_retriever