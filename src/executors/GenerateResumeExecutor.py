
import db.connectors.userInfo.UserJobInfo
from db.connectors.userInfo.IUserJobInfo import IUserJobInfo
from models.PromptItem import PromptItem


class GenerateResumeExecutor:
    def __init__(self, user_info: IUserJobInfo):
        self.user_info = user_info

    async def execute(self, promptItem: PromptItem):
        user_info = self.user_info.get_user_info(promptItem.user_id)

        retrieve_relevant_info(promptItem.url, user_info)

        augment_info()

        generate_resume()


        NotImplementedError()