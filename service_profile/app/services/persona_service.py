from typing import List
from app.entities.persona import Persona
from app.repositories.mongo_repository import save_to_mongo, fetch_from_mongo
from app.utils.base64_encoder import encode_name
from app.usecases.create_query import create_query

async def create_persona_profile(persona: Persona):
    """Create and save a persona profile.

    Args:
        persona (Persona): The persona profile data.

    Returns:
        dict: Success status.
    """
    key = encode_name(persona.nome)
    data = persona.dict()
    await save_to_mongo(key, data, "persona_info")
    return {"status": "success"}

async def get_persona_profile(fields: List[str]):
    """Retrieve persona profile data based on requested fields.

    Args:
        fields (list[str]): List of fields to retrieve.

    Returns:
        dict: Profile data for the specified fields.
    """
    query = create_query(fields)
    return await fetch_from_mongo(query, "persona_info")
