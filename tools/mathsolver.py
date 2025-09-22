
from langchain.tools import tool 
@tool 
def mathsolver_tool(expression : str)-> str:
    "Your are helpful model for math expression solve this expression provide correct solution of nay math proplem "
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Exception error is {str(e)} ."