from pydantic import BaseModel

class JobsAndInfo(BaseModel):
    job: str
    info: list