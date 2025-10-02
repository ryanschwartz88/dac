"""Vector index management for SourceDAC."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List


class Indexer:
    """Handle interactions with the ChromaDB vector store."""

    def __init__(self, index_dir: Path) -> None:
        """Initialize the indexer with the path to the `.dac/index` directory."""
        self.index_dir = index_dir

    def initialize_collection(self) -> None:
        """Create or load the ChromaDB collection."""
        raise NotImplementedError

    def index_documents(self, documents: Iterable[str]) -> None:
        """Chunk and upsert markdown content into the vector store."""
        raise NotImplementedError

    def query_index(self, query_text: str, k: int = 5) -> List[str]:
        """Return the `k` most relevant text chunks for a query."""
        raise NotImplementedError

