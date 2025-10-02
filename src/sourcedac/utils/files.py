"""Filesystem utilities for SourceDAC."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List


def parse_dacignore(path: Path) -> List[str]:
    """Parse the `.dacignore` file and return glob patterns."""
    raise NotImplementedError


def iter_project_files(project_root: Path, ignore_patterns: Iterable[str]) -> Iterable[Path]:
    """Yield project files excluding those matching ignore patterns."""
    raise NotImplementedError

