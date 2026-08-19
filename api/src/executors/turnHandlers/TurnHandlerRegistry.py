
from src.executors.turnHandlers.ITurnHandler import ITurnHandler
from src.executors.turnHandlers.TurnType import TurnType
from src.db.currentSession.ICurrentSession import ICurrentSession
from src.data_models.PromptItem import PromptItem

class TurnHandlerRegistry:

    def __init__(self, handlers: dict[TurnType, ITurnHandler]):
        self._handlers = handlers

    def resolve(self, prompt_item: PromptItem, curr_sess: ICurrentSession) -> ITurnHandler:
        turn_type = self._classify(prompt_item, curr_sess)
        handler = self._handlers.get(turn_type)

        if handler is None:
            raise ValueError(f"No handler registered for turn type: {turn_type}")
        return handler

    def _classify(self, prompt_item: PromptItem, curr_sess: ICurrentSession) -> TurnType:
        if curr_sess.job_description is None or prompt_item.job_description_changed:
            return TurnType.NEW_JOB
        return TurnType.REFINEMENT