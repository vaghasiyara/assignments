from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.submissions import router as submission_router
from app.routes.admin import router as admin_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(submission_router)
app.include_router(admin_router)


