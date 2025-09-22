############## Math  Solver API Request #################

from fastapi import FastAPI
import requests
from pydantic import BaseModel
from agents.mathagent import get_agent_executor



app = FastAPI()


class AgentRequest(BaseModel):
    query: str


agent_executor = get_agent_executor()

@app.post('/ask')
async def UserInput(request: AgentRequest):
    """Endpoint to ask a question to the AI agent."""
    try:
        # We need to use the agent_executor variable to invoke it.
        # The invoke method takes a dictionary as input, not just a string.
        response = await agent_executor.invoke({"input": request.query})
        
        # Return the final output from the agent's response
        return {"response": response.get("output")}
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}