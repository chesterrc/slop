from db.DatabaseDependencies import get_user_job_info_db
from executors.GenerateResumeExecutor import GenerateResumeExecutor


def build_resume_executor() -> GenerateResumeExecutor:
    user_info_db = get_user_job_info_db()
    return GenerateResumeExecutor(user_info_db)

resume_executor = build_resume_executor()