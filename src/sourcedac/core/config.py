"""Configuration utilities for SourceDAC."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Optional


class ConfigError(Exception):
    """Raised when configuration loading fails."""


class ConfigLoader:
    """Load configuration from environment and config files."""

    def __init__(self, project_root: Optional[Path] = None) -> None:
        """Initialize the loader.

        Args:
            project_root: Optional path to the project root.
        """
        self.project_root = project_root

    def load(self) -> Dict[str, Any]:
        """Load configuration values using precedence rules."""
        raise NotImplementedError

    def load_project_config(self) -> Dict[str, Any]:
        """Load the project-specific config from `.dac/config.yaml`."""
        raise NotImplementedError

    def load_global_config(self) -> Dict[str, Any]:
        """Load the user-level config from `~/.config/sourcedac/config.yaml`."""
        raise NotImplementedError

    def init_llm_client(self, config: Dict[str, Any]) -> Any:
        """Initialize the LLM abstraction client via litellm."""
        raise NotImplementedError

