from src.executors.retrieval.Retriever import Retriever
from src.executors.turnHandlers.ITurnHandler import ITurnHandler
from src.data_models.

class NewJobTurnHandler(ITurnHandler):
    def __init__(self,
                 retriever: Retriever,
                 llm_client: IModel):
        self._retriever = retriever
        self._llm_client = llm_client

    async def handle(self, prompt_item, user_profile, curr_sess) -> ResumeTurnResponse:
        self._retriever.embed(prompt_item, user_profile)
        #