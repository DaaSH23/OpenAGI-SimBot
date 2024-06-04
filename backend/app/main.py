from fastapi import FastAPI
from app.api.routes import auth as auth_routes
from app.api.routes import stack as stack_routes
from app.api.routes import workflow as workflow_routes
from app.api.database import database, engine
import app.api.models as models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# Endpoint for creating users
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])

# Endpoint for creating stack
app.include_router(stack_routes.router, prefix="/stack", tags=["stack"])

app.include_router(workflow_routes.router, prefix="/workflow", tags=["workflow"])

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()