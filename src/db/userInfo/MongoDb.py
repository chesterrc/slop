from IUserJobInfo import IUserJobInfo
from data_models.UserInfo import UserInfo

class UserJobInfo(IUserJobInfo):
    def __init__(self):
        #connect with mongo db?
        pass

    async def get_user_info(self, user_id: int) -> UserInfo:
        NotImplementedError()