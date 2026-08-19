from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.utils.Composition import executor_composition
from src.data_models.PromptItem import PromptItem
from src.data_models.UserInfo import UserInfo

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await executor_composition.close()

app = FastAPI(title="SLOP", lifespan=lifespan)

@app.post("/generate/user-resume")
async def generate_user_resume(
        prompt: PromptItem
):
    executor = await executor_composition.get_generate_resume_executor()
    return await executor.execute_resume_generation(prompt)

@app.put("/resume")
async def place_resume(user_info: UserInfo):
    executor = await executor_composition.get_generate_resume_executor()
    return await executor.execute_resume_upload(user_info)