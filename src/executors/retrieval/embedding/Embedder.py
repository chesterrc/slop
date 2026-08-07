from sentence_transformers import SentenceTransformer

from data_models import PromptItem
from executors.retrieval.embedding.IEmbedder import IEmbedder

class Embedder(IEmbedder):
    def __init__(self):
        self._embedding_model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2",
            prompts={
                "retrieval": "Retrieve semantically similar text:"
            }
        )

    def encode(self, prompt: PromptItem):
        econded_prompt = self._embedding_model.encode(prompt)
