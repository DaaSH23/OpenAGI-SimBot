from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
from app.api import schemas

from openagi.actions.files import WriteFileAction
from openagi.actions.tools.ddg_search import DuckDuckGoSearch
from openagi.agent import Admin
from openagi.llms.openai import OpenAIModel
from openagi.planner.task_decomposer import TaskPlanner

# Set the OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = ""

# Initialize the LLM
config = OpenAIModel.load_from_env_config()
llm = OpenAIModel(config=config, model_name="gpt-3.5-turbo")

# Setup an Admin Agent
admin = Admin(
    llm=llm,
    actions=[
        DuckDuckGoSearch,
        WriteFileAction,
    ],
    planner=TaskPlanner(
        human_intervene=False,
    ),
)

router = APIRouter()

@router.post("/run-agent")
async def run_agent(request: schemas.AgentRequest):
    try:
        # Run the Agent with the query and description from the request
        res = admin.run(
            query=request.query,
            description=request.description,
        )
        return {"result": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

