from enum import Enum

from fastapi import Depends
from typing import Annotated

class DatabaseType(str, Enum):
    MONGO = "mongo"

def get_user_job_info_db():
    NotImplementedError()