from pydantic import BaseModel

class PersonalInfo(BaseModel):
    full_name: str
    email: str
    phone_number: str
    location: str
    links: list[str]