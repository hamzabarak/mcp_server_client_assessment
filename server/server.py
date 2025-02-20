from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
import subprocess
import ollama

# Initialize FastAPI app and FastMCP
app = FastAPI()
mcp = FastMCP(app)

# Define the input model for the tool
class UserQuery(BaseModel):
    query: str

# Define the tool to process user queries
@mcp.tool()
async def process_query(input: UserQuery):
    """
    Processes a user query using Ollama to generate and execute a system command.
    """
    try:
        # Use Ollama to generate a system command based on the user query
        prompt = f"Generate a safe system command for the following query: '{input.query}'"
        response = ollama.complete(model="llama3.2", prompt=prompt)

        # Extract the generated command from the response
        command = response['choices'][0]['text'].strip()

        # Execute the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return {"command": command, "output": result.stdout}
        else:
            return {"command": command, "error": result.stderr}
    except Exception as e:
        return {"error": str(e)}

# Run the MCP server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
