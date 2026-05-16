import os

# Must be set BEFORE any other imports
os.environ["TRANSFORMERS_CACHE"] = "/tmp/hf_cache"
os.environ["HF_HOME"] = "/tmp/hf_home"
os.environ["SENTENCE_TRANSFORMERS_HOME"] = "/tmp/st_cache"
os.environ["HF_DATASETS_CACHE"] = "/tmp/datasets_cache"

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="SHL Assessment Recommender",
    version="1.0.0",
)

app.include_router(router)