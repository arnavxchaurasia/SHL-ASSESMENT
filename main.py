import os

os.environ["TRANSFORMERS_CACHE"] = "/tmp/hf_cache"
os.environ["HF_HOME"] = "/tmp/hf_home"

from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="SHL Assessment Recommender",
    version="1.0.0",
)

app.include_router(router)