# SourceDAC

> Transform software development and documentation into an automated, real-time symbiotic process.

## 🎯 Vision & Mission

### Vision
To fundamentally change the relationship between software development and documentation, transforming it from a manual chore into an automated, real-time symbiotic process.

### Mission
To provide developers and AI agents with a perpetually current and context-aware understanding of a codebase, accelerating development, improving code quality, and eliminating documentation debt. SourceDAC achieves this by creating a live, lifecycle-aware context engine that operates directly within a project's repository.

## 🚨 The Problem

Software development is plagued by a context gap. As codebases grow, understanding the "why" behind the code becomes exponentially harder. This leads to several critical problems:

- **Stale Documentation**: Manually written documentation inevitably becomes outdated, misleading developers and slowing down onboarding.
- **Architectural Drift**: The original design intent is lost over time as new features are added and refactors occur without updating a central source of truth.
- **Limited AI Context**: AI coding assistants are powerful but are constrained by limited context windows. They must re-analyze code for every complex request, often missing the high-level architectural picture, leading to suboptimal suggestions.

## 💡 The Solution: A Lifecycle-Aware Context Engine

SourceDAC is a developer tool that treats documentation as a first-class, automated citizen of the software development lifecycle. It operates as a CLI (`dac`) that creates and maintains a rich, dual-purpose Context Store within a hidden `.dac/` directory in your project.

This tool is lifecycle-aware, providing different value propositions depending on the project's state:

### 🔮 Ideation State (No Code)
For new projects, `dac init` acts as a Socratic architect, guiding the developer through a wizard to create foundational design documents (`MISSION.md`, `ARCHITECTURE_PROPOSAL.md`) before any code is written.

### 🏗️ Generation State (Existing Code)
For existing projects, `dac generate` performs a deep, one-time analysis to generate a comprehensive baseline of documentation and architectural understanding.

### 🔄 Iteration State (Active Development)
`dac dev` runs in the background, watching for file changes and incrementally updating the Context Store in real-time while simultaneously serving the MCP server for AI integration.

## ⚡ Core Features

### The Context Store
The heart of SourceDAC, located in the `.dac/` directory.

- **Human-Readable Markdown** (`.dac/markdown/`): A full suite of documentation, from high-level architecture to function descriptions, version-controlled in Git.
- **Machine-Readable Vector Index** (`.dac/index/`): A local, lightning-fast semantic search index (ChromaDB) of the documentation, designed to be queried by AI agents.

### The CLI (`dac`)

| Command | Description |
|---------|-------------|
| `dac init` | Initializes SourceDAC, creating the `.dac/` structure and configuration. Launches the "Ideation" wizard for new projects. |
| `dac generate` | Performs the deep analysis of an existing codebase to populate the Context Store. |
| `dac dev` | The primary command for active development. It starts a background process that both monitors source files for changes and launches the local MCP server. |
| `dac query "[INQUIRY]"` | Performs a semantic search on the documentation store. |
| `dac optimize "[INSTRUCTION]"` | Enriches a simple instruction with relevant context to create a "super-prompt". |

### The MCP (Machine Consumption Protocol)
A local API server, started via `dac dev`, that exposes two key endpoints for AI agents:

- `POST /query`: Allows an AI to perform semantic search on the Context Store.
- `POST /optimize`: Allows an AI to request a context-enriched prompt.

### Intelligent Ignoring
A `.dacignore` file, with syntax identical to `.gitignore`, allows developers to specify files and directories (like `node_modules/`, `dist/`, or the `.dac/` folder itself) that the watcher and generator should ignore.

## 🛠️ Technical Architecture

| Component | Technology |
|-----------|------------|
| **Language** | Python 3.10+ |
| **CLI Framework** | Typer |
| **LLM Abstraction** | litellm, enabling flexible, user-provided API keys and model choices via a layered configuration system (Environment Variables > Project Config > Global Config) |
| **Code Parsing** | tree-sitter for robust, multi-language static analysis |
| **Vector Store** | ChromaDB (running locally) |
| **File Watcher** | watchdog |
| **MCP Server** | FastAPI |

## 🚀 Getting Started

### 1. Installation
```bash
# Install the SourceDAC CLI from a package manager (e.g., PyPI)
pip install sourcedac
```

### 2. Setup
```bash
# Navigate to your project directory
cd /path/to/your/project

# Set up your LLM API keys (e.g., for OpenAI)
export OPENAI_API_KEY="sk-..."
```

### 3. Initialize SourceDAC
```bash
# Initialize SourceDAC in your project
# This creates the .dac/ directory, config.yaml, and a .dacignore file.
dac init
```

### 4. Generate Documentation
```bash
# To generate docs for an existing project:
dac generate
```

### 5. Start Development Mode
```bash
# To start the live development mode for active coding:
dac dev
```

---

*SourceDAC: Where code meets context, and documentation becomes intelligent.*