# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Python Environment - CRITICAL

**Always use UV** for Python operations. Never use `python -m`, `pip install`, or `python script.py` directly.

```bash
# Correct usage
uv run pytest                    # Run tests
uv run pytest -m unit            # Run unit tests only
uv pip install -e ".[dev]"       # Install in development mode
uv run python script.py          # Execute scripts

# WRONG - Do NOT use these
python -m pytest                 # ❌
pip install package              # ❌
python script.py                 # ❌
```

## Essential Development Commands

### Setup & Installation
```bash
make install          # Install in development mode (editable)
make verify           # Verify installation (package, plugin, health)
make doctor           # Run health check diagnostics
```

### Testing
```bash
make test                                # Run full test suite
uv run pytest                            # Alternative test command
uv run pytest -m unit                    # Unit tests only
uv run pytest -m integration             # Integration tests only
uv run pytest tests/unit/test_file.py    # Single test file
uv run pytest --cov=superclaude          # With coverage report
uv run pytest -v                         # Verbose output
```

### Code Quality
```bash
make lint            # Run ruff linter (check code)
make format          # Format code with ruff
make clean           # Remove build artifacts
```

### Plugin Development
```bash
make build-plugin         # Build plugin artifacts into dist/
make sync-plugin-repo     # Sync artifacts into ../SuperClaude_Plugin
```

### Additional Utilities
```bash
make translate       # Translate README to Chinese and Japanese (using Neural CLI)
```

## Project Architecture

### High-Level Structure

SuperClaude is a **meta-programming configuration framework** that transforms Claude Code through:
- **Behavioral instruction injection** (via CLAUDE.md)
- **Component orchestration** (pytest plugin + slash commands)
- **Systematic workflow automation** (PM Agent patterns)

Current version **4.1.9** is a Python package with pytest plugin and optional slash commands.
**v5.0** (planned) will introduce TypeScript plugin system.

### Directory Layout

```
SuperClaude_Framework/
├── src/superclaude/           # Main Python package
│   ├── pytest_plugin.py       # Auto-loaded pytest integration
│   ├── pm_agent/              # Pre/post implementation patterns
│   │   ├── confidence.py      # Pre-execution confidence assessment
│   │   ├── self_check.py      # Post-implementation validation
│   │   ├── reflexion.py       # Error learning and prevention
│   │   └── token_budget.py    # Token allocation management
│   ├── execution/             # Parallel execution framework
│   │   ├── parallel.py        # Wave→Checkpoint→Wave pattern
│   │   ├── reflection.py      # Meta-reasoning
│   │   └── self_correction.py # Error recovery
│   ├── cli/                   # Command-line interface
│   │   ├── main.py            # superclaude command entry point
│   │   ├── doctor.py          # Health check diagnostics
│   │   ├── install_commands.py # Command installation
│   │   └── install_mcp.py     # MCP server installation
│   ├── agents/                # 16 specialized agent definitions (.md)
│   ├── commands/              # 30 slash command definitions (.md)
│   ├── modes/                 # 7 behavioral mode definitions (.md)
│   ├── hooks/                 # Hook configurations
│   ├── mcp/                   # MCP server configurations
│   ├── core/                  # Core framework files (FLAGS, PRINCIPLES, RULES)
│   ├── skills/                # Runtime skills (e.g., confidence-check)
│   └── scripts/               # Utility scripts
├── tests/                     # Test suite
│   ├── unit/                  # Unit tests
│   │   ├── test_confidence.py
│   │   ├── test_self_check.py
│   │   ├── test_reflexion.py
│   │   └── test_token_budget.py
│   ├── integration/           # Integration tests
│   │   └── test_pytest_plugin.py
│   └── conftest.py            # Shared pytest fixtures
├── plugins/superclaude/       # Future TypeScript plugins (v5.0 - NOT ACTIVE)
├── docs/                      # Documentation
│   ├── developer-guide/       # Development guides
│   ├── user-guide/           # User documentation
│   └── reference/            # API reference & troubleshooting
├── scripts/                   # Analysis tools (workflow metrics, A/B testing)
└── [Root Files]
    ├── PLANNING.md           # Architecture & absolute rules (READ FIRST)
    ├── TASK.md               # Current tasks & priorities
    ├── KNOWLEDGE.md          # Accumulated insights & troubleshooting
    ├── CONTRIBUTING.md       # Contribution guidelines
    ├── AGENTS.md             # Repository guidelines
    └── CLAUDE.md             # Claude Code specific rules
```

### Key Architectural Patterns

#### 1. PM Agent Patterns (Core Philosophy)
Three patterns that define SuperClaude's approach:

**ConfidenceChecker** (`src/superclaude/pm_agent/confidence.py`)
- Pre-execution confidence assessment before starting work
- ≥90%: Proceed with implementation
- 70-89%: Present alternatives, continue investigation
- <70%: STOP - ask questions, investigate more
- ROI: 25-250x token savings by preventing wrong-direction work

**SelfCheckProtocol** (`src/superclaude/pm_agent/self_check.py`)
- Post-implementation evidence-based validation
- No speculation - verify with tests/docs
- Four validation questions + seven red flags

**ReflexionPattern** (`src/superclaude/pm_agent/reflexion.py`)
- Error learning and prevention across sessions
- Cross-session pattern matching
- Automatic error categorization

#### 2. Parallel Execution Framework
**Wave → Checkpoint → Wave pattern** (`src/superclaude/execution/parallel.py`)
- 3.5x faster than sequential execution
- Automatic dependency analysis
- Example: [Read files in parallel] → Analyze → [Edit files in parallel]

#### 3. Plugin Architecture (Current v4.1.9)
- Pytest plugin auto-loaded via `pyproject.toml` entry points
- CLI commands via `[project.scripts]`
- Slash commands installed to `~/.claude/commands/`

## Testing Philosophy

### Pytest Markers
Tests automatically get markers based on directory structure:
- Tests in `/unit/` → `@pytest.mark.unit`
- Tests in `/integration/` → `@pytest.mark.integration`

Custom markers for PM Agent patterns:
- `@pytest.mark.confidence_check` - Pre-execution confidence assessment
- `@pytest.mark.self_check` - Post-implementation validation
- `@pytest.mark.reflexion` - Error learning tests
- `@pytest.mark.complexity("simple|medium|complex")` - Token budget tests

### Test Fixtures
Available via pytest plugin (see `src/superclaude/pytest_plugin.py`):
- `confidence_checker` - Confidence assessment fixture
- `self_check_protocol` - Validation protocol fixture
- `reflexion_pattern` - Error learning fixture
- `token_budget` - Token allocation fixture
- `pm_context` - PM Agent context fixture

### Coverage Focus
Coverage configured in `pyproject.toml` to focus on `src/superclaude/`.
Always run tests with coverage: `uv run pytest --cov=superclaude`

## Git Workflow

### Branch Structure
- `master` - Production-ready code
- `integration` - Testing branch before master
- `feature/*`, `fix/*`, `docs/*` - Development branches

### Standard Workflow
1. Create branch from `integration`: `git checkout -b feature/your-feature`
2. Develop with tests: `uv run pytest`
3. Commit with conventional commits: `git commit -m "feat: description"`
4. Merge to `integration` → validate → merge to `master`

### Parallel Development with Git Worktrees
When running multiple sessions simultaneously, use git worktrees to avoid conflicts:

```bash
# Create worktree for integration branch
cd ~/github/SuperClaude_Framework
git worktree add ../SuperClaude_Framework-integration integration

# Create worktree for feature branch
git worktree add ../SuperClaude_Framework-feature feature/pm-agent

# Cleanup when done
git worktree remove ../SuperClaude_Framework-integration
```

## Core Development Principles

### 1. Evidence-Based Development
**Never guess** - always verify with official sources:
- Use Context7 MCP for official documentation
- Check existing code before implementing
- Verify assumptions against test results

### 2. Confidence-First Implementation
Check confidence BEFORE starting work:
- ≥90%: Proceed
- 70-89%: Present alternatives
- <70%: STOP and investigate

ROI: Spend 100-200 tokens on confidence check to save 5,000-50,000 tokens on wrong direction.

### 3. Parallel-First Execution
Use Wave → Checkpoint → Wave pattern when operations are independent:
- Reading multiple files
- Batch transformations
- Parallel searches

**When NOT to use**: Operations with dependencies or sequential analysis.

### 4. Token Efficiency
Allocate tokens based on task complexity:
- **Simple** (typo fix): 200 tokens
- **Medium** (bug fix): 1,000 tokens
- **Complex** (feature): 2,500 tokens

### 5. No Hallucinations
Use SelfCheckProtocol's Four Questions:
1. Are all tests passing? (show output)
2. Are all requirements met? (list items)
3. No assumptions without verification? (show docs)
4. Is there evidence? (test results, code changes)

Avoid Seven Red Flags:
- "Tests pass" without output
- "Everything works" without evidence
- "Implementation complete" with failing tests
- Skipping error messages
- Ignoring warnings
- Hiding failures
- "Probably works" language

## Package Structure & Entry Points

### Package Information
- **Name**: `superclaude`
- **Version**: 4.1.9 (from `VERSION` file)
- **Python**: >=3.10
- **Build system**: hatchling (PEP 517)

### Entry Points (pyproject.toml)
```toml
[project.scripts]
superclaude = "superclaude.cli.main:main"

[project.entry-points.pytest11]
superclaude = "superclaude.pytest_plugin"
```

### Dependencies
**Core**:
- pytest>=7.0.0
- click>=8.0.0
- rich>=13.0.0

**Development** (`[dev]` extras):
- pytest-cov>=4.0.0
- pytest-benchmark>=4.0.0
- scipy>=1.10.0 (for A/B testing)
- black>=22.0
- ruff>=0.1.0
- mypy>=1.0

## Code Style & Quality

### Python Style
- **Formatter**: Black (line length 88)
- **Linter**: Ruff with rules E, F, I, N, W
- **Type checking**: mypy (gradual typing)
- **Indentation**: 4 spaces
- **Naming**: snake_case for modules/functions, PascalCase for classes

### Quality Commands
```bash
make lint       # Run ruff check
make format     # Run ruff format
```

### Pre-commit Hooks
Configured in `.pre-commit-config.yaml` - run before commits automatically.

## MCP Server Integration

SuperClaude integrates with 8 MCP servers via **airis-mcp-gateway**:

**High Priority**:
- **Tavily** - Primary web search (Deep Research)
- **Context7** - Official documentation lookup
- **Sequential-Thinking** - Multi-step reasoning (30-50% token reduction)
- **Serena** - Session persistence & memory

**Optional**:
- **Playwright** - Browser automation
- **Magic** - UI component generation
- **Morphllm-Fast-Apply** - Context-aware code modifications
- **Chrome DevTools** - Performance analysis

### MCP Installation
```bash
superclaude mcp --list              # List available servers
superclaude mcp                     # Interactive installation
superclaude mcp --servers tavily    # Install specific server
```

## Documentation Structure

Essential documentation to read before contributing:

| Document | Purpose | When to Read |
|----------|---------|--------------|
| **PLANNING.md** | Architecture, design principles, absolute rules | Session start, before implementation |
| **TASK.md** | Current tasks, priorities, backlog | Daily, before starting work |
| **KNOWLEDGE.md** | Accumulated insights, best practices, troubleshooting | When encountering issues |
| **CONTRIBUTING.md** | Contribution guidelines, workflow | Before submitting PRs |
| **AGENTS.md** | Repository guidelines | Referenced by existing rules |

Additional documentation:
- `docs/developer-guide/` - Technical implementation guides
- `docs/user-guide/` - Feature usage and workflows
- `docs/reference/` - API reference and troubleshooting

## Installation Methods

### For Users (v4.1.9)
```bash
# Option 1: pipx (recommended)
pipx install superclaude
superclaude install

# Option 2: Direct from repo
git clone https://github.com/SuperClaude-Org/SuperClaude_Framework.git
cd SuperClaude_Framework
./install.sh
```

### For Developers
```bash
# Install in editable mode
make install

# Verify installation
make verify

# Run health check
make doctor
```

## Important Context Files

When working with this repository, be aware of these context files that guide behavior:

- **CLAUDE.md** - Claude Code specific rules and workflow
- **PLANNING.md** - Architecture and absolute rules (READ FIRST)
- **TASK.md** - Current development tasks
- **KNOWLEDGE.md** - Accumulated project insights
- **AGENTS.md** - Repository guidelines from rules

These files should be consulted when making architectural decisions or implementing features.

## Future Roadmap

### v5.0 (Planned - Issue #419)
- TypeScript plugin system
- Project-local `.claude-plugin/` detection
- Plugin marketplace distribution
- Enhanced MCP server integration

Current implementation uses Python package with pytest plugin and slash commands.
TypeScript plugin directories (`plugins/superclaude/`) exist but are **NOT ACTIVE** in v4.1.9.
