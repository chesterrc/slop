from pydantic import BaseModel

class Education(BaseModel):
    institution_name: str
    degree: str
    field_of_study: str
    graduation_date: str
