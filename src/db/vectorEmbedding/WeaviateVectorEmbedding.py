from weaviate import WeaviateAsyncClient
from weaviate.classes.query import Filter

from src.db.vectorEmbedding.IVectorEmbedding import IVectorDb

class WeaviateVectorEmbedding(IVectorDb):
    def __init__(self, client: WeaviateAsyncClient, collection_name: str = "AccomplishmentChunks"):
        self._client = client
        self._collection_name = collection_name

    async def upsert_embedding(self, chunk_id: str, vector: list[float], metadata: dict) -> None:
        collection = self._client.collections.get(self._collection_name)
        await collection.data.replace(uuid=chunk_id, properties=metadata, vector=vector)

    async def similarity_search(
        self, query_vector: list[float], top_k: int, filter: dict | None = None
    ) -> list[RetrievedChunk]:
        collection = self._client.collections.get(self._collection_name)

        weaviate_filter = None
        if filter:
            conditions = [Filter.by_property(k).equal(v) for k, v in filter.items()]
            weaviate_filter = conditions[0]
            for cond in conditions[1:]:
                weaviate_filter = weaviate_filter & cond

        results = await collection.query.near_vector(
            near_vector=query_vector,
            limit=top_k,
            filters=weaviate_filter,
            return_metadata=["distance"],
        )

        return [
            RetrievedChunk(
                id=str(obj.uuid),
                score=1 - obj.metadata.distance,  # cosine distance -> similarity
                metadata=obj.properties,
            )
            for obj in results.objects
        ]