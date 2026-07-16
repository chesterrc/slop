from fastapi import FastAPI, Depends
from models.PromptItem import PromptItem
from executors.GenerateResumeExecutor import GenerateResumeExecutor

app = FastAPI()

@app.post("/generate/user-resume")
async def generate_user_resume(prompt: PromptItem, generate_resume_executor: GenerateResumeExecutor = Depends(GenerateResumeExecutor)):
    response = await generate_resume_executor.execute(prompt)
    return response

