# SuperClaude Setup Guide for New Projects

This guide explains how to set up SuperClaude's memory and MCP server integration for any new project.

## Quick Reference

| Component | What It Does | Setup Required |
|-----------|--------------|----------------|
| `/sc:*` commands | Slash commands for workflows | One-time install |
| ReflexionMemory | Auto-records pytest failures | Directory creation |
| Serena MCP | Session persistence & code understanding | Per-project config |
| Sequential Thinking | Multi-step reasoning | Per-project config |
| Tavily | Web search | Per-project config + API key |

---

## Step 1: One-Time Global Installation

Run this once on your machine:

```bash
# Install SuperClaude
pipx install superclaude

# Install slash commands to ~/.claude/commands/
superclaude install

# Verify installation
superclaude doctor
```

This gives you access to all `/sc:*` commands in any project.

---

## Step 2: Per-Project Directory Setup

For each new project, create the memory directories:

```bash
cd /path/to/your-project

# Create memory directories
mkdir -p docs/memory
mkdir -p docs/mistakes

# Initialize empty memory files (optional - auto-created on first use)
touch docs/memory/solutions_learned.jsonl
touch docs/memory/patterns_learned.jsonl
```

### Directory Structure

```
your-project/
├── .serena/                    # Created by Serena MCP
│   ├── project.yml            # Serena config
│   ├── memories/              # Session memories (persisted by Serena)
│   └── cache/                 # Language server cache
├── docs/
│   ├── memory/
│   │   ├── solutions_learned.jsonl  # Error solutions (pytest auto-records)
│   │   ├── patterns_learned.jsonl   # Success patterns
│   │   ├── pm_context.md            # Project context (manual)
│   │   └── last_session.md          # Session notes (manual)
│   └── mistakes/                     # Detailed error analysis docs
└── CLAUDE.md                         # Project instructions
```

---

## Step 3: Configure MCP Servers for the Project

Add the following to `~/.claude.json` under the `projects` key for your project path:

### Option A: Manual Edit

Open `~/.claude.json` and find (or create) your project entry:

```json
{
  "projects": {
    "/path/to/your-project": {
      "allowedTools": [],
      "mcpContextUris": [],
      "mcpServers": {
        "sequential-thinking": {
          "type": "stdio",
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
          "env": {}
        },
        "serena": {
          "type": "stdio",
          "command": "uvx",
          "args": [
            "--from",
            "git+https://github.com/oraios/serena",
            "serena",
            "start-mcp-server",
            "--context",
            "ide-assistant",
            "--project",
            "/path/to/your-project"
          ],
          "env": {}
        },
        "tavily": {
          "type": "stdio",
          "command": "npx",
          "args": ["-y", "tavily-mcp"],
          "env": {
            "TAVILY_API_KEY": "your-tavily-api-key"
          }
        }
      },
      "hasTrustDialogAccepted": true,
      "hasCompletedProjectOnboarding": true
    }
  }
}
```

### Option B: Use Claude Code CLI

```bash
# Add Serena MCP server
claude mcp add serena \
  --type stdio \
  --command uvx \
  --args "--from" "git+https://github.com/oraios/serena" "serena" "start-mcp-server" "--context" "ide-assistant" "--project" "/path/to/your-project"

# Add Sequential Thinking
claude mcp add sequential-thinking \
  --type stdio \
  --command npx \
  --args "-y" "@modelcontextprotocol/server-sequential-thinking"
```

---

## Step 4: Initialize Serena for the Project

On first use, Serena creates its config. You can also manually initialize:

```bash
cd /path/to/your-project

# Create .serena directory structure
mkdir -p .serena/memories
mkdir -p .serena/cache

# Create basic project.yml
cat > .serena/project.yml << 'EOF'
languages:
- python
- typescript
encoding: "utf-8"
ignore_all_files_in_gitignore: true
ignored_paths: []
read_only: false
excluded_tools: []
initial_prompt: ""
project_name: "your-project-name"
included_optional_tools: []
EOF
```

---

## Step 5: Add to .gitignore

```gitignore
# Serena cache (don't commit)
.serena/cache/

# SuperClaude memory (optional - commit if you want team sharing)
# docs/memory/solutions_learned.jsonl
# docs/memory/workflow_metrics.jsonl
```

---

## Step 6: Add Memory Protocol to CLAUDE.md

Add this to your project's `CLAUDE.md` to make Claude use the memory system:

```markdown
## Memory Integration

### Session Start Protocol
At the start of each session:
1. Read `docs/memory/solutions_learned.jsonl` for past error solutions
2. Read `docs/memory/pm_context.md` for project context (if exists)
3. Proactively mention relevant past errors when encountering similar issues

### Error Handling Protocol
When encountering errors:
1. Check `docs/memory/solutions_learned.jsonl` for similar errors first
2. If found, apply the known solution
3. If new error, investigate and append solution to `solutions_learned.jsonl`

### Session End Protocol
Before ending significant sessions:
1. Update `docs/memory/pm_context.md` with important discoveries
2. Run `/sc:save` to persist session context (if Serena available)
```

---

## How Each Component Works

### ReflexionMemory (Pytest Integration)

**Automatic** - When tests with `@pytest.mark.reflexion` fail, errors are recorded:

```python
import pytest

@pytest.mark.reflexion
def test_my_feature():
    # If this fails, error auto-saved to solutions_learned.jsonl
    assert calculate() == expected
```

Run tests:
```bash
uv run pytest tests/ -v
```

### Serena MCP

**Commands** that use Serena:
- `/sc:load` - Load project context and memories
- `/sc:save` - Save session discoveries

**Tools** Serena provides:
- `activate_project` - Initialize project context
- `read_memory` / `write_memory` - Persist memories
- `find_symbol` - Code navigation
- `find_referencing_code_snippets` - Find usages

### Sequential Thinking

Automatically activated for complex analysis tasks. Provides structured multi-step reasoning.

---

## Verification Checklist

After setup, verify everything works:

```bash
# 1. Check Claude Code sees the MCP servers
claude mcp list

# Expected output should include:
# - serena
# - sequential-thinking
# - tavily (if configured)

# 2. Check directories exist
ls -la docs/memory/
ls -la .serena/

# 3. Test pytest integration (if you have tests)
uv run pytest tests/ -v --collect-only | head -20

# 4. Check solutions file
cat docs/memory/solutions_learned.jsonl | head -5
```

---

## Troubleshooting

### Serena not connecting

1. **Check the project path** - Must be absolute path, must match exactly
2. **Restart Claude Code** - MCP servers load at startup
3. **Check uvx is installed**: `which uvx`

### Memories not persisting

1. **Check `.serena/memories/` directory exists**
2. **Verify Serena is in `claude mcp list`**
3. **Try `/sc:load` explicitly**

### ReflexionMemory not recording

1. **Check test markers**: Use `@pytest.mark.reflexion`
2. **Check directory exists**: `docs/memory/`
3. **Run pytest directly**: `uv run pytest tests/ -v`

---

## Complete Setup Script

Copy and run this for any new project:

```bash
#!/bin/bash
# superclaude-setup.sh - Run in your project root

PROJECT_PATH=$(pwd)
PROJECT_NAME=$(basename "$PROJECT_PATH")

# Create directories
mkdir -p docs/memory
mkdir -p docs/mistakes
mkdir -p .serena/memories
mkdir -p .serena/cache

# Create Serena config
cat > .serena/project.yml << EOF
languages:
- python
- typescript
encoding: "utf-8"
ignore_all_files_in_gitignore: true
ignored_paths: []
read_only: false
excluded_tools: []
initial_prompt: ""
project_name: "$PROJECT_NAME"
included_optional_tools: []
EOF

# Create .gitignore entries
echo "# Serena cache" >> .gitignore
echo ".serena/cache/" >> .gitignore

# Initialize memory files
touch docs/memory/solutions_learned.jsonl
touch docs/memory/patterns_learned.jsonl

echo "SuperClaude directories created for: $PROJECT_NAME"
echo ""
echo "NEXT STEP: Add MCP servers to ~/.claude.json"
echo ""
echo "Add this to ~/.claude.json under projects[\"$PROJECT_PATH\"].mcpServers:"
echo ""
cat << 'MCPCONFIG'
{
  "sequential-thinking": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"],
    "env": {}
  },
  "serena": {
    "type": "stdio",
    "command": "uvx",
    "args": [
      "--from",
      "git+https://github.com/oraios/serena",
      "serena",
      "start-mcp-server",
      "--context",
      "ide-assistant",
      "--project",
MCPCONFIG
echo "      \"$PROJECT_PATH\""
cat << 'MCPCONFIG2'
    ],
    "env": {}
  }
}
MCPCONFIG2
```

Save as `superclaude-setup.sh` and run: `bash superclaude-setup.sh`

---

## Summary

| Step | Action | Frequency |
|------|--------|-----------|
| 1 | `pipx install superclaude && superclaude install` | Once per machine |
| 2 | Create `docs/memory/` and `docs/mistakes/` | Once per project |
| 3 | Add MCP servers to `~/.claude.json` | Once per project |
| 4 | Initialize `.serena/` directory | Once per project |
| 5 | Add memory protocol to `CLAUDE.md` | Once per project |

After setup, the system works automatically via pytest integration and slash commands.
