from pydantic import BaseModel

class JobsAndInfo(BaseModel):
    title: str
    start_date: str
    end_date: str
    bullets: list[str]