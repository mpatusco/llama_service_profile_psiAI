from app.entities.psico import Psico
from app.repositories.mongo_repository import save_to_mongo
from app.utils.base64_encoder import encode_name

async def create_psico_profile(psico: Psico):
    """Create and save a psychologist profile with an empty conversation list.

    Args:
        psico (Psico): The psychologist profile data.

    Returns:
        dict: Success status.
    """
    key = encode_name(f"{psico.nome}{psico.registro}")
    data = psico.dict()
    data['conversas'] = []
    await save_to_mongo(key, data, "psico_info")
    return {"status": "success"}
