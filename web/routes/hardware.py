from fastapi import APIRouter
from monitoring.collector import collect_hardware

router = APIRouter()

@router.get('/hardware')
def get_hardware():
    return collect_hardware()