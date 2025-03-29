from fastapi import FastAPI
from .routers import routing

app = FastAPI(
	title='Metrogo',
	description='A simple, fast and intelligent subway router',
	version='0.1.0',
)

app.include_router(routing.router, prefix='/v1/routing', tags=['routing version 1'])
