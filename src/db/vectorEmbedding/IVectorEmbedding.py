from abc import ABC, abstractmethod

@abstractmethod
class IVectorDb(ABC):
    @abstractmethod
    async def get_vector(self):
        raise NotImplementedError()