# Warp MCP Server Setup Guide

MCP servers have been configured for Warp at `~/.warp/claude.json`

## Installed MCP Servers

### ✅ Ready to Use (No API Key Required)

1. **context7** - Official library documentation lookup
   - Automatically provides official docs for libraries and frameworks
   - No setup required

2. **sequential-thinking** - Multi-step reasoning
   - Enables structured analysis and debugging
   - 30-50% token reduction for complex tasks
   - No setup required

3. **playwright** - Browser automation
   - E2E testing and browser automation
   - No setup required

4. **chrome-devtools** - Performance analysis
   - Real-time browser inspection and debugging
   - No setup required

### 🔑 Requires API Key

5. **tavily** - Web search for research
   - **FREE TIER AVAILABLE** at https://app.tavily.com
   - Required for `/research` commands and current information
   
   **Setup Steps:**
   ```bash
   # 1. Get free API key at https://app.tavily.com
   # 2. Add to your shell profile (~/.zshrc or ~/.bashrc):
   export TAVILY_API_KEY="tvly-your_api_key_here"
   
   # 3. Reload your shell:
   source ~/.zshrc  # or source ~/.bashrc
   ```

6. **serena** - Session persistence & memory
   - Semantic code understanding
   - Requires Python 3.9+ and uvx (already using uv in this project)
   - No API key required, but needs uv package manager

## Verification

After restarting Warp, verify MCP servers are connected:

```bash
# The MCP servers will activate automatically when needed
# No manual verification command needed for Warp
```

## Optional Servers (Not Configured)

These paid services are available but not configured by default:

- **magic** - UI component generation (requires TWENTYFIRST_API_KEY from 21st.dev)
- **morphllm-fast-apply** - Bulk code transformations (requires MORPH_API_KEY)

To add these, edit `~/.warp/claude.json` and add API keys to your environment.

## Server Activation

MCP servers activate automatically based on your requests:

| Request Type | Activated Servers |
|--------------|-------------------|
| Library documentation | context7 |
| Complex debugging | sequential-thinking |
| Browser testing | playwright |
| Performance issues | chrome-devtools |
| Web research | tavily + sequential-thinking |
| Large projects | serena |

## Troubleshooting

### Servers Not Working

1. **Check Node.js version** (need v16+):
   ```bash
   node --version
   ```

2. **Check uv installation** (for Serena):
   ```bash
   uv --version
   ```

3. **Restart Warp** after configuration changes

4. **Check API key** (for Tavily):
   ```bash
   echo $TAVILY_API_KEY
   ```

### Common Issues

- **Tavily not working**: Get free API key at https://app.tavily.com
- **Serena errors**: Ensure uv is installed (already in this project)
- **NPX errors**: Update Node.js to latest LTS version

## Next Steps

1. ✅ MCP configuration file created at `~/.warp/claude.json`
2. 🔑 Get Tavily API key (free): https://app.tavily.com
3. 🔄 Add Tavily key to `~/.zshrc`: `export TAVILY_API_KEY="tvly-..."`
4. 🔄 Restart Warp terminal
5. ✨ MCP servers will activate automatically!

## Benefits

- **Context7**: No more hallucinated API docs
- **Sequential**: Better debugging and analysis
- **Playwright**: Real browser testing
- **Tavily**: Current information and research
- **Serena**: Project memory across sessions
- **Chrome DevTools**: Performance insights

Enjoy enhanced AI assistance with MCP servers! 🚀
