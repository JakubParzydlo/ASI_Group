from api.services import kedro
from api import APIRouter

router = APIRouter()

@router.get("/raw_data")
async def raw_data():
    return kedro.raw_data()