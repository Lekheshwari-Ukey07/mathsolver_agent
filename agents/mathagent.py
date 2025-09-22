# mathagent and excecutor 
import os 
from dotenv import load_dotenv

# agents/mathagent.py

import os 
from dotenv import load_dotenv
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from tools.mathsolver import mathsolver_tool 
# Load environment variables
load_dotenv()
os.getenv("OPENAI_API_KEY")

# Define the tools
tools = [mathsolver_tool]

# Configure the LLM
llm = ChatOpenAI(temperature=0.6, model="gpt-3.5-turbo")

# Define the ReAct prompt template
template = """
You are a helpful assistant that can solve math problems. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now have the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""

prompt = PromptTemplate.from_template(template)

# Create the agent executor instance once
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


# Define the function that returns the executor
# The name MUST be exactly 'get_agent_executor'
def get_agent_executor():
    """Returns the configured agent executor instance."""
    return agent_executor