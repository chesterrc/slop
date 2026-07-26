from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.utils.Composition import executor_composition
from data_models.PromptItem import PromptItem

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
    return await executor.execute(prompt)

