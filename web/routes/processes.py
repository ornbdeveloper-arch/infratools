from fastapi import APIRouter
from monitoring.collector import collect_processes

router = APIRouter()

@router.get("/processes")
def get_processes():
    return collect_processes()