# client.py
import asyncio
from fastmcp import Client

async def main():
    async with Client("weather.py") as mcp_client:
        tools = await mcp_client.list_tools()
        print("📦 Available tools:", tools)

if __name__ == "__main__":
    asyncio.run(main())
