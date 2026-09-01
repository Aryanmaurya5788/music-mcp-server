from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP(
    "Music Demo",
    host="0.0.0.0",
    port=int(os.environ.get("PORT", "10000")),
)


@mcp.tool()
def create_song(title: str, genre: str, mood: str) -> str:
    """Create a demo song request."""
    return (
        f"Song request created!\n"
        f"Title: {title}\n"
        f"Genre: {genre}\n"
        f"Mood: {mood}\n\n"
        "This is a demo MCP server. No real music was generated."
    )


@mcp.tool()
def get_song_status() -> str:
    """Return the demo song generation status."""
    return "Demo song status: completed"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
