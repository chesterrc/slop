import asyncpg

from IUserJobInfo import IUserJobInfo
from data_models.UserInfo import UserInfo

class PostgresUserInfo(IUserJobInfo):
    def __init__(self, pool: asyncpg.Pool):
        self._pool = pool

    async def get_user_info(self, user_id: int) -> UserInfo:
        NotImplementedError()