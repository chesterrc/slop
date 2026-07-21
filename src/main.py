from fastapi import FastAPI, Depends
from Pooling import resume_executor
from data_models.PromptItem import PromptItem
from executors.GenerateResumeExecutor import GenerateResumeExecutor

app = FastAPI()

@app.post("/generate/user-resume")
async def generate_user_resume(
        prompt: PromptItem
):
    return await resume_executor.execute(prompt)

