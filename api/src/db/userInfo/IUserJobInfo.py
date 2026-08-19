from abc import ABC, abstractmethod
from data_models.UserInfo import UserInfo

class IUserJobInfo(ABC):
    @abstractmethod
    async def get_user_info(self, user_id: int) -> UserInfo:
        raise NotImplementedError

    @abstractmethod
    async def upsert_user_info(self, user_info: UserInfo) -> None:
        raise NotImplementedError


