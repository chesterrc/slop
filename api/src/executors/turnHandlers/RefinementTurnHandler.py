from src.executors.turnHandlers.ITurnHandler import ITurnHandler

class RefinementTurnHandler(ITurnHandler):
    def __init__(self,
                 retriever: IRetriever,
                 llm_client: IModel):
        self._retriever = retriever
        self._llm_client = llm_client

    async def handle(self, prompt_item, user_profile, curr_sess) -> ResumeTurnResponse:
        raise NotImplementedError()