from fastapi import APIRouter

router = APIRouter()

@router.get("/search")
async def search_for_doc():
    pass


