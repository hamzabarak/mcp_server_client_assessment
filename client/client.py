import asyncio
import aiohttp
from mcp import ClientSession
from pydantic import BaseModel

# Define the base URL of the MCP server
# SERVER_URL = "http://localhost:8000"
SERVER_URL = "http://127.0.0.1:8000"

# Define the input model for user queries
class UserQuery(BaseModel):
    query: str

async def send_query(query_text):
    """
    Sends a user query to the MCP server and receives the command execution result.
    """
    async with aiohttp.ClientSession() as session:
        try:
            # Prepare request payload
            payload = {"query": query_text}

            # Send request to MCP server
            async with session.post(f"{SERVER_URL}/tools/process_query/invoke", json=payload) as response:
                if response.status == 200:
                    result = await response.json()
                    return result
                else:
                    return {"error": f"Failed to process query. Status Code: {response.status}"}
        
        except Exception as e:
            return {"error": str(e)}

async def main():
    """
    Main function to interact with the user and process queries.
    """
    while True:
        # Get user input
        user_input = input("Enter your query (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Exiting MCP Client...")
            break

        # Send the query to the MCP server
        result = await send_query(user_input)

        # Display results
        if "command" in result:
            print(f"\nGenerated Command: {result['command']}")
            if "output" in result:
                print(f"Command Output: {result['output']}\n")
            elif "error" in result:
                print(f"Command Error: {result['error']}\n")
        elif "error" in result:
            print(f"Error: {result['error']}\n")

if __name__ == "__main__":
    asyncio.run(main())
