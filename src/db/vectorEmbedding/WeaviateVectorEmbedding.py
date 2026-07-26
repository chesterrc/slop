from weaviate import WeaviateAsyncClient
from weaviate.classes.query import Filter
from weaviate.classes.config import Configure, Property, DataType

from src.db.vectorEmbedding.IVectorEmbedding import IVectorDb

class WeaviateVectorEmbedding(IVectorDb):
    def __init__(self, client: WeaviateAsyncClient, collection_name: str = "AccomplishmentChunks"):
        self._client = client
        self._collection_name = collection_name

    async def create_accomplishment_collection(client: WeaviateAsyncClient) -> None:
        await client.collections.create(
            name="AccomplishmentChunks",
            vector_config=Configure.Vectors.text2vec_weaviate(),  # Weaviate Cloud's own embedding service
            properties=[
                Property(name="user_id", data_type=DataType.TEXT),
                Property(name="job_id", data_type=DataType.TEXT),
                Property(name="job_title", data_type=DataType.TEXT),
                Property(name="company", data_type=DataType.TEXT),
                Property(name="type", data_type=DataType.TEXT),
                Property(name="text", data_type=DataType.TEXT),
            ],
        )

    async def upsert_embedding(self, chunk_id: str, vector: list[float], metadata: dict) -> None:
        collection = self._client.collections.get(self._collection_name)
        await collection.data.replace(uuid=chunk_id, properties=metadata)

    async def similarity_search(self, query_text: str, top_k: int, filter: dict | None = None) -> list[RetrievedChunk]:
        collection = self._client.collections.get(self._collection_name)

        weaviate_filter = None
        if filter:
            conditions = [Filter.by_property(k).equal(v) for k, v in filter.items()]
            weaviate_filter = conditions[0]
            for cond in conditions[1:]:
                weaviate_filter = weaviate_filter & cond

        results = await collection.query.near_text(
            query=query_text,
            limit=top_k,
            filters=weaviate_filter,
            return_metadata=["distance"],
        )

        return [
            RetrievedChunk(id=str(obj.uuid), score=1 - obj.metadata.distance, metadata=obj.properties)
            for obj in results.objects
        ]