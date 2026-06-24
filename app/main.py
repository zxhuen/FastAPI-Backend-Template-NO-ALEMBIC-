from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.database import engine, Base
from app.api.routes.post import router as post_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # runs on startup
    Base.metadata.create_all(bind=engine)
    yield
    # runs on shutdown (optional cleanup)


app = FastAPI(
    title="FastAPI with SQLAlchemy and PostgreSQL Template",
    lifespan=lifespan
)

app.include_router(post_router)