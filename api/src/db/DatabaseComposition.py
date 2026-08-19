# app/composition/database_composition.py
import asyncio
import asyncpg
from pymongo import AsyncMongoClient
from pymongo.asynchronous.database import AsyncDatabase

from src.db.currentSession import ICurrentSession, MongoCurrentSession
from src.db.userInfo import IUserJobInfo, PostgresUserInfo

class DatabaseComposition:
    def __init__(self):
        self._curr_session_client: AsyncMongoClient | None = None
        self._curr_session_db: AsyncDatabase | None = None

        self._user_info_pool: asyncpg.Pool | None = None
        self._user_info_pool_lock = asyncio.Lock()

        self._curr_sess: ICurrentSession.ICurrentSession
        self._user_info_repo: IUserJobInfo.IUserJobInfo

    async def get_curr_session_db(self) -> AsyncDatabase:
        if self._curr_session_db is None:
            async with self._curr_session_db:
                if self._curr_session_db is None:
                    #TODO: Grab DBs from environment
                    client = AsyncMongoClient(...)
                    await client.admin.command("ping")
                    self._curr_session_client = client
                    self._curr_session_db = client[...]
        return self._curr_session_db

    async def get_user_info_pool(self) -> asyncpg.Pool:
        if self._user_info_pool is None:
            async with self._user_info_pool_lock:
                if self._user_info_pool is None:
                    #TODO: idk if the user is gonna have admin privilege if I just hardcode it, look into it
                    self._user_info_pool = await asyncpg.create_pool(database="postgres", user=...)
        return self._user_info_pool

    async def get_curr_session(self) -> ICurrentSession:
        if self._curr_session_db is None:
            db = await self.get_curr_session_db()
            self._curr_sess = MongoCurrentSession.MongoCurrentSession(db)
        return self._curr_sess

    async def get_user_info(self) -> IUserJobInfo:
        if self._user_info_repo is None:
            pool = await self.get_user_info_pool()
            self._user_info_repo = PostgresUserInfo.PostgresUserInfo(pool)
        return self._user_info_repo