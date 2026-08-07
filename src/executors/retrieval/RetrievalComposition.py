import asyncio
from weaviate import WeaviateAsyncClient
from weaviate.connect import ConnectionParams

from src.executors.retrieval.Retriever import Retriever
from src.db.vectorEmbedding.WeaviateVectorEmbedding import WeaviateVectorEmbedding
from src.db.vectorEmbedding.IVectorEmbedding import IVectorDb
from src.executors.retrieval.embedding.IEmbedder import IEmbedder
from src.executors.retrieval.embedding.Embedder import Embedder

class RetrievalComposition:

    def __init__(self):
        self._vector_client: WeaviateAsyncClient | None = None
        self._vector_client_lock = asyncio.Lock()
        self._vector_db: IVectorDb | None = None
        self._embedding_client: IEmbedder | None = None
        self._job_match_retriever: Retriever | None = None

    async def get_vector_client(self) -> WeaviateAsyncClient:
        if self._vector_client is None:
            async with self._vector_client_lock:
                if self._vector_client is None:
                    #TODO: Add params for auth in .env
                    client = WeaviateAsyncClient(
                        connection_params=ConnectionParams.from_params(
                            http_host="localhost",
                            http_port=8099,
                            http_secure=False,
                            grpc_host="localhost",
                            grpc_port=50052,
                            grpc_secure=False,
                        )
                    )
                    await client.connect()  # verify connectivity
                    self._vector_client = client
        return self._vector_client

    async def get_vector_db(self) -> IVectorDb:
        if self._vector_db is None:
            client = await self.get_vector_client()
            self._vector_db = WeaviateVectorEmbedding(client=client)
        return self._vector_db

    def get_embedding_client(self) -> IEmbedder:
        if self._embedding_client is None:
            self._embedding_client = Embedder()
        return self._embedding_client

    async def get_job_match_retriever(self) -> Retriever:
        if self._job_match_retriever is None:
            vector_db = await self.get_vector_db()
            self._job_match_retriever = Retriever(
                vector_db=vector_db,
                embedding_client=self.get_embedding_client(),
            )
        return self._job_match_retriever