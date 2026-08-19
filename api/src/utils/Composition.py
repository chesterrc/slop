from executors.turnHandlers.NewJobTurnHandler import NewJobTurnHandler
from executors.turnHandlers.RefinementTurnHandler import RefinementTurnHandler
from src.db.DatabaseComposition import DatabaseComposition
from src.executors.retrieval.RetrievalComposition import RetrievalComposition
from src.executors.turnHandlers.TurnType import TurnType
from src.executors.turnHandlers.NewJobTurnHandler import NewJobTurnHandler
from src.executors.turnHandlers.RefinementTurnHandler import RefinementTurnHandler
from src.executors.ResumeExecutor import ResumeExecutor
from src.executors.turnHandlers.TurnHandlerRegistry import TurnHandlerRegistry


class Compose:
    def __init__(self, database: DatabaseComposition, retrieval: RetrievalComposition):
        self._database = database
        self._retrieval = retrieval
        self._turn_handler_registry: TurnHandlerRegistry | None = None
        self._generate_resume_executor: ResumeExecutor | None = None

    async def get_turn_handler_registry(self) -> TurnHandlerRegistry:
        if not self._turn_handler_registry:
            self._turn_handler_registry = TurnHandlerRegistry({
                TurnType.NEW_JOB: NewJobTurnHandler(
                    self._retrieval.get_job_match_retriever(),
                    ...
                ),
                TurnType.REFINEMENT: RefinementTurnHandler(
                    self._retrieval.get_job_match_retriever(),
                    ...
                ),
            })
        return self._turn_handler_registry

    async def get_generate_resume_executor(self) -> ResumeExecutor:
        if not self._generate_resume_executor:
            self._generate_resume_executor = ResumeExecutor(
                user_info_db=await self._database.get_user_info(),
                curr_session_db=await self._database.get_curr_session(),
                turn_handler_registry=await self._turn_handler_registry.get_turn_handler_registry()
            )
        return self._generate_resume_executor

    async def close(self) -> None:
        await self._database.close()

database_composition = DatabaseComposition()
retrieval_composition = RetrievalComposition()
executor_composition = Compose(database_composition, retrieval_composition)