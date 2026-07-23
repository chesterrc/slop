from abc import ABC, abstractmethod

from src.data_models.CurrSessItem import CurrSessItem

class ICurrentSession(ABC):
    @abstractmethod
    async def get_curr_sess(self, user_id: int) -> CurrSessItem:
        raise NotImplementedError
