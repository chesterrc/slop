
import asyncio

from src.db.userInfo.IUserJobInfo import IUserJobInfo
from src.db.currentSession.ICurrentSession import ICurrentSession
from executors.TurnHandlers.TurnHandlerRegistry import TurnHandlerRegistry
from data_models.PromptItem import PromptItem


class GenerateResumeExecutor:
    def __init__(self,
                 user_info_db: IUserJobInfo,
                 curr_session_db: ICurrentSession,
                 turn_handler_registry: TurnHandlerRegistry
                 ):
        self._user_info_db = user_info_db
        self._curr_session = curr_session_db
        self._turn_handler_registry = turn_handler_registry

    async def execute(self, prompt_item: PromptItem):
        user_profile, curr_sess = await asyncio.gather(
            self._user_info_db.get_user_info(prompt_item.user_id),
            self._curr_session.get_current_session(prompt_item.user_id)
        )

        handler = self._turn_handler_registry.resolve(prompt_item, curr_sess)
        response = await handler.handle(prompt_item, user_profile, curr_sess)

        curr_sess.current_draft = response.draft if response.draft is not None else None

        await self._curr_session.append_turn(
            user_id=prompt_item.user_id,
            user_message=prompt_item.prompt,
            assistant_message=response.commentary,
            current_draft=curr_sess.current_draft
        )

        return ChatResponse(reply=response.commentary, draft=curr_sess.current_draft)
