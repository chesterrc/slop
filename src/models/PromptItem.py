from pydantic import BaseModel

class PromptItem(BaseModel):
    user_id: int
    url: str
    prompt: str
