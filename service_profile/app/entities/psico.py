from pydantic import BaseModel

class Psico(BaseModel):
    """Data model for a psychologist profile.

    Attributes:
        nome (str): Name of the psychologist.
        registro (str): Registration number of the psychologist.
    """
    nome: str
    registro: str
