from fastapi import FastAPI
from app.routes import branch
from app.utils.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Banking Application API", version="1.0.0")
app.include_router(branch.router, prefix="/branches", tags=["Branches"])