from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.pages.api.model.predict_api import router as v1_router
from src.pages.api.model.predict_api_v2 import router as v2_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router)
app.include_router(v2_router) 