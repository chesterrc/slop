from abc import ABC, abstractmethod

class IEmbedder(ABC):
    @abstractmethod
    def encode(self, prompt: str):
        raise NotImplementedError
