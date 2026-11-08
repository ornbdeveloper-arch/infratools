from fastapi import APIRouter
from monitoring.collector import collect_network

router = APIRouter()

@router.get("/network")
def get_network():
    return collect_network()