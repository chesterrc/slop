
import db.connectors.userInfo.UserInfo

from models.PromptItem import PromptItem


class GenerateResumeExecutor:
    def __init__(self):
        pass

    async def execute(self, promptItem: PromptItem):
        user_info = UserInfo.get_user_info(promptItem.user_id)

        retrieve_relevant_info(promptItem.url, user_info)

        augment_info()

        generate_resume()


        NotImplementedError()