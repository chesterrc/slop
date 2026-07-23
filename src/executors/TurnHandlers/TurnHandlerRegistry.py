from enum import Enum

from ITurnHandler import ITurnHandler
from src.data_models.PromptItem import PromptItem

class TurnType(str, Enum):
    NEW_JOB = "new_job"
    REFINEMENT = "refinement"

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