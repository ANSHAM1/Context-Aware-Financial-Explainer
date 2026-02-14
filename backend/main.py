from fastapi import FastAPI
from config import settings
from routers.explain import router as explain_router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(
    explain_router,
    prefix=settings.API_V1_STR,
    tags=["Financial Explanation"]
)


@app.get("/")
def root():
    return {"message": "Financial Explainer Backend Running"}