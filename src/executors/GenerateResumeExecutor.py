
import asyncio

from db.connectors.userInfo.IUserJobInfo import IUserJobInfo
from data_models.PromptItem import PromptItem


class GenerateResumeExecutor:
    def __init__(self,
                 user_info_db: IUserJobInfo,
                 curr_session_db: ICurrentSession,
                 retriever: IRetriever,
                 model_client: IModelClient ):
        self._user_info_db = user_info_db
        self._curr_session = curr_session_db
        self._retriever = retriever
        self._model_client = model_client


    async def execute(self, prompt_item: PromptItem):
        user_profile, curr_sess = await asyncio.gather(
            self._user_info_db.get_user_info(prompt_item.user_id),
            self._user_info_db.get_current_session(prompt_item.user_id)
        )

        relevant_history = self._retriever.retrieve_relevant(message, top_k = 5)
        prompt = PromptBuilder.build_promopt(
            user_profile,
            curr_sess,
            relevant_history
        )

        reply = await self._model_client.get_model_reply(prompt)
        await self._curr_session.append_message(prompt_item.user_id, prompt_item.message, reply)
    
        return ChatResponse(reply, matches)

        prompt = build_prompt(session)


        NotImplementedError()