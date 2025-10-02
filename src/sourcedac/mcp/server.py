"""FastAPI MCP server for SourceDAC."""

from __future__ import annotations

from fastapi import FastAPI

from sourcedac.core.indexer import Indexer

app = FastAPI(title="SourceDAC MCP Server")


@app.on_event("startup")
async def on_startup() -> None:
    """Initialize resources when the server starts."""
    raise NotImplementedError


@app.post("/query")
async def query_endpoint(query: str) -> dict:
    """Perform a semantic search against the context store."""
    raise NotImplementedError


@app.post("/optimize")
async def optimize_endpoint(instruction: str) -> dict:
    """Return a context-enriched instruction for downstream LLMs."""
    raise NotImplementedError

