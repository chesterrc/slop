from pydantic import BaseModel

class UserInfo(BaseModel):
    user_id: int
    jobs_and_info: list