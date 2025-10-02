"""Command-line interface for SourceDAC."""

from __future__ import annotations

from typing import Optional

import typer

from sourcedac.core import analysis
from sourcedac.core import config
from sourcedac.core import indexer
from sourcedac.core import watcher
from sourcedac.mcp import server

app = typer.Typer(help="SourceDAC CLI entry point")


@app.callback()
def main(ctx: typer.Context) -> None:
    """Initialize CLI context and shared resources."""
    ctx.obj = {}


@app.command()
def init(path: Optional[str] = typer.Option(None, help="Path to initialize SourceDAC")) -> None:
    """Initialize SourceDAC in the current project."""
    typer.echo("Initializing SourceDAC...")


@app.command()
def generate() -> None:
    """Generate baseline documentation and context."""
    typer.echo("Running generate pipeline...")


@app.command()
def dev() -> None:
    """Run live development mode with watcher and MCP server."""
    typer.echo("Starting development mode...")


@app.command()
def query(inquiry: str = typer.Argument(..., help="Search query")) -> None:
    """Query the context store."""
    typer.echo(f"Querying context store for: {inquiry}")


@app.command()
def optimize(instruction: str = typer.Argument(..., help="Instruction to optimize")) -> None:
    """Generate an optimized instruction prompt."""
    typer.echo(f"Optimizing instruction: {instruction}")

