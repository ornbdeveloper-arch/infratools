from fastapi import APIRouter
from monitoring.collector import collect_system

router = APIRouter()

@router.get("/system")
def get_system():
    return collect_system()
