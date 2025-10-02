"""File watching utilities for SourceDAC development mode."""

from __future__ import annotations

from pathlib import Path
from typing import Callable, Iterable


class Watcher:
    """Monitor file changes and trigger incremental analysis."""

    def __init__(self, project_root: Path, on_change: Callable[[Iterable[Path]], None]) -> None:
        """Initialize the watcher.

        Args:
            project_root: Root of the project to watch.
            on_change: Callback invoked with paths that changed.
        """
        self.project_root = project_root
        self.on_change = on_change

    def start(self) -> None:
        """Start the watcher loop."""
        raise NotImplementedError

    def stop(self) -> None:
        """Stop the watcher loop."""
        raise NotImplementedError

