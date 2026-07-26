from executors.TurnHandlers.NewJobTurnHandler import NewJobTurnHandler
from executors.TurnHandlers.RefinementTurnHandler import RefinementTurnHandler
from src.db.DatabaseComposition import DatabaseComposition
from src.executors.TurnHandlers.TurnType import TurnType
from src.executors.TurnHandlers.NewJobTurnHandler import NewJobTurnHandler
from src.executors.TurnHandlers.RefinementTurnHandler import RefinementTurnHandler
from src.executors.GenerateResumeExecutor import GenerateResumeExecutor
from src.executors.TurnHandlers.TurnHandlerRegistry import TurnHandlerRegistry


class Compose:
    def __init__(self, database: DatabaseComposition):
        self._database = database
        self._turn_handler_registry: TurnHandlerRegistry | None = None
        self._generate_resume_executor: GenerateResumeExecutor | None = None

    async def get_turn_handler_registry(self) -> TurnHandlerRegistry:
        if not self._turn_handler_registry:
            self._turn_handler_registry = TurnHandlerRegistry({
                TurnType.NEW_JOB: NewJobTurnHandler(),
                TurnType.REFINEMENT: RefinementTurnHandler(),
            })
        return self._turn_handler_registry

    async def get_generate_resume_executor(self) -> GenerateResumeExecutor:
        if not self._generate_resume_executor:
            self._generate_resume_executor = GenerateResumeExecutor(
                user_info_db=await self._database.get_user_info(),
                curr_session_db=await self._database.get_curr_session(),
                turn_handler_registry=await self._turn_handler_registry.get_turn_handler_registry()
            )
        return self._generate_resume_executor

    async def close(self) -> None:
        await self._database.close()

databse_composition = DatabaseComposition()
executor_composition = Compose(databse_composition)