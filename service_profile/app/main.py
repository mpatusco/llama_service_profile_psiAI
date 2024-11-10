from fastapi import FastAPI
from app.api.v1 import persona_routes, psico_routes

"""FastAPI main application.

This file initializes the FastAPI application and includes routers for handling 
requests related to persona and psychologist profiles.

Attributes:
    app (FastAPI): The main FastAPI application instance.
"""

app = FastAPI()

app.include_router(persona_routes.router, prefix="/api/v1/persona")
app.include_router(psico_routes.router, prefix="/api/v1/psico")

