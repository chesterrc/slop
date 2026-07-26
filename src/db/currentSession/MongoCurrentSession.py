from pymongo.asynchronous.database import AsyncDatabase

from src.db.currentSession import ICurrentSession
from src.data_models.CurrSessItem import CurrSessItem

class MongoCurrentSession(ICurrentSession):
    def __init__(self, db: AsyncDatabase):
        self._curr_sess_db = None

    async def get_curr_sess(self, user_id: int) -> CurrSessItem:
        raise NotImplementedError
