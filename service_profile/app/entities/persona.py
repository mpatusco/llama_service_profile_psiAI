from pydantic import BaseModel

class Persona(BaseModel):
    """Data model for a persona profile.

    Attributes:
        nome (str): Name of the persona.
        idade (int): Age of the persona.
        persona (str): Persona type.
        diagnostico (str): Diagnosis information.
        profissao (str): Profession of the persona.
        problemas (str): Issues the persona is facing.
        local (str): Location of the persona.
    """
    nome: str
    idade: int
    persona: str
    diagnostico: str
    profissao: str
    problemas: str
    local: str
