from typing import List
from fastapi import APIRouter, HTTPException
from app.services.persona_service import create_persona_profile, get_persona_profile
from app.entities.persona import Persona

router = APIRouter()

@router.post("/")
async def create_persona(persona: Persona):
    """Create a persona profile.

    Args:
        persona (Persona): The persona profile data.

    Returns:
        dict: Status of the profile creation.

    Raises:
        HTTPException: If there's an error in the process.
    """
    try:
        return await create_persona_profile(persona)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
async def get_persona(nome: str):
    """Retrieve persona profile data based on specific fields.

    Args:
        fields (list[str]): The list of fields to fetch for the persona profile.

    Returns:
        dict: The requested profile data.

    Raises:
        HTTPException: If there's an error in the process.
    """
    try:
        return await get_persona_profile(nome)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
