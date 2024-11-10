from fastapi import APIRouter, HTTPException
from app.services.psico_service import create_psico_profile
from app.entities.psico import Psico

router = APIRouter()

@router.post("/")
async def create_psico(psico: Psico):
    """Create a psychologist profile.

    Args:
        psico (Psico): The psychologist profile data.

    Returns:
        dict: Status of the profile creation.

    Raises:
        HTTPException: If there's an error in the process.
    """
    try:
        return await create_psico_profile(psico)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
