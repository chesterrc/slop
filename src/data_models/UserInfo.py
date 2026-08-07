from pydantic import BaseModel

from src.data_models.JobsAndInfo import JobsAndInfo
from src.data_models.PersonalInfo import PersonalInfo
from src.data_models.Education import Education

class UserInfo(BaseModel):
    user_id: int
    personal_info: PersonalInfo
    work_experience: list[JobsAndInfo]
    education: list[Education]
    Other: list[str]