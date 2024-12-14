from fastapi import APIRouter

from ..chat import router as chat_router
from ..stt import stt as stt_router
from ..tts import tts as tts_router
from .endpoints import images, models

api_router = APIRouter()
api_router.include_router(stt_router.router)
api_router.include_router(tts_router.router)
api_router.include_router(models.router)
api_router.include_router(images.router)
api_router.include_router(chat_router.router)
