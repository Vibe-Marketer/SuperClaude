# Understanding Memory Systems in SuperClaude

## Overview: Two Memory Systems

SuperClaude has **two different memory systems** that work together:

### 1. ReflexionMemory (Built-in) ✅
- **Always available** - no installation needed
- **Built into SuperClaude Framework**
- Stores error history and solutions locally
- Location: `docs/memory/reflexion.jsonl`
- Used by PM Agent for error learning

### 2. Mindbase MCP (Optional Enhancement) 🔧
- **Optional external service** - requires installation
- **Semantic search** across ALL conversation history
- Powered by PostgreSQL + pgvector + qwen3-embedding
- Cross-project knowledge sharing
- Requires: `airis-mcp-gateway` with "recommended" profile

## What is Mindbase?

**Mindbase** is an optional MCP server that provides **semantic memory** - it can search through all your past conversations to find relevant context, even if you used different words.

### Key Differences from ReflexionMemory

| Feature | ReflexionMemory (Built-in) | Mindbase MCP (Optional) |
|---------|---------------------------|-------------------------|
| **Availability** | Always available | Requires installation |
| **Search Type** | Keyword-based (50% overlap) | Semantic (AI-powered) |
| **Storage** | Local file (reflexion.jsonl) | PostgreSQL database |
| **Scope** | Error history only | All conversations |
| **Cross-Project** | No | Yes |
| **Installation** | Built-in | External MCP server |

### When Do You Need Mindbase?

**You DON'T need Mindbase if:**
- You're just getting started
- Working on single projects
- Error learning is sufficient (ReflexionMemory)

**You MIGHT want Mindbase if:**
- Working on many related projects
- Want to search ALL past conversations semantically
- Need cross-project knowledge sharing
- Working on long-term projects (months/years)

## Installation Status

**Currently NOT installed** in your Warp configuration.

### How to Install Mindbase (Optional)

Mindbase is part of the **airis-mcp-gateway** system:

```bash
# Install airis-mcp-gateway with recommended profile
# See: https://github.com/agiletec-inc/airis-mcp-gateway

# Installation steps (example - check official docs):
git clone https://github.com/agiletec-inc/airis-mcp-gateway
cd airis-mcp-gateway

# Use "recommended" profile (includes mindbase)
# OR use "minimal" profile (excludes mindbase for lightweight setup)
```

### Adding Mindbase to Warp Configuration

If you install airis-mcp-gateway, add to `~/.warp/claude.json`:

```json
{
  "mcpServers": {
    // ... existing servers ...
    "mindbase": {
      "command": "node",
      "args": ["/path/to/airis-mcp-gateway/server.js"],
      "env": {
        "AIRIS_PROFILE": "recommended"
      }
    }
  }
}
```

## How SuperClaude Uses Memory

### Automatic Error Learning (ReflexionMemory)

When an error occurs:
1. **PM Agent** detects the error
2. **ReflexionMemory** searches for similar past errors (keyword-based)
3. If found: Suggests previous solutions
4. If new: Records error and solution for future
5. Stored in: `docs/memory/reflexion.jsonl`

### Semantic Search (Mindbase - if installed)

When Mindbase is available:
1. Claude can search ALL past conversations semantically
2. Finds relevant context even with different wording
3. Example: Search "authentication issues" finds conversations about "login problems"
4. Works across ALL projects stored in the database

## Recommendation

**For most users**: Start with **built-in ReflexionMemory** only. It provides:
- ✅ Error learning and prevention
- ✅ Zero configuration
- ✅ Fast and lightweight
- ✅ Project-scoped memory

**Consider Mindbase later** if you:
- Work on many interconnected projects
- Need cross-project knowledge discovery
- Want semantic search of all conversations
- Have PostgreSQL expertise for maintenance

## Current Setup

Your current Warp MCP configuration includes:
- ✅ context7 (official docs)
- ✅ sequential-thinking (multi-step reasoning)
- ✅ playwright (browser automation)
- ✅ chrome-devtools (performance)
- ✅ tavily (web search with your API key configured)
- ✅ serena (code understanding)

**NOT included:**
- ❌ mindbase (optional semantic memory)
- ❌ magic (paid UI generation)
- ❌ morphllm (paid code transformations)

This is a **great starting setup** with all the free, essential tools configured!

## Summary

**Mindbase** is an optional, advanced memory system for semantic search across all conversations. You **don't need it** to use SuperClaude effectively - the built-in **ReflexionMemory** handles error learning automatically.

Think of it as:
- **ReflexionMemory**: Your project's error notebook
- **Mindbase**: Your entire conversation library with AI-powered search

Both work together when Mindbase is installed, but ReflexionMemory works perfectly on its own.
