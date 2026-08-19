from abc import ABC, abstractmethod

from src.db.currentSession.ICurrentSession import ICurrentSession
from src.data_models.PromptItem import PromptItem
from src.data_models.UserInfo import UserInfo

class ITurnHandler(ABC):
    @abstractmethod
    async def handle(
        self,
        prompt_item: PromptItem,
        user_profile: UserInfo,
        curr_sess: ICurrentSession,
    ) -> ResumeTurnResponse:
        raise NotImplementedError