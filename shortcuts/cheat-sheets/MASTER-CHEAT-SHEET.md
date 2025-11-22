now that i have all that # 🚀 QUICK REFERENCE CHEAT SHEET

Everything you need to know in one place.

---

## 🐳 DOCKER SERVICES (Run from ANYWHERE)

### Start Services
```bash
archon-start          # Start Archon (runs in background)
mindbase-start        # Start Mindbase (runs in background)
```

### Stop Services
```bash
archon-stop           # Stop Archon
mindbase-stop         # Stop Mindbase
```

### Check Status
```bash
archon-status         # Is Archon running?
mindbase-status       # Is Mindbase running?
docker ps             # See all running containers
```

### ⚡ Key Points:
- ✅ Run these commands from ANY directory
- ✅ Services run in background (close terminals freely)
- ✅ Work on any project while they run
- ❌ DON'T navigate to repos and stay there
- ❌ DON'T keep terminals open

**Think of it like Spotify**: Start it once, it runs in background, work on other stuff.

---

## 🤖 SUPERCLAUDE SLASH COMMANDS

### The Main One (Use This!)
```
/pm [your task]
```
**Example:** `/pm add user authentication with JWT`

What it does:
- Checks confidence before starting (≥90% to proceed)
- Looks up official docs (no guessing)
- Asks questions if unsure
- Validates after implementation
- **Saves 25-250x tokens**

---

### Most Useful Commands

| Command | Use For | Example |
|---------|---------|---------|
| `/pm` | Any coding task | `/pm build a REST API` |
| `/research` | Deep research | `/research React Server Components` |
| `/index-repo` | Index codebase (1x per project) | `/index-repo` |
| `/implement` | Build features | `/implement dark mode toggle` |
| `/test` | Generate/run tests | `/test authentication module` |
| `/troubleshoot` | Debug errors | `/troubleshoot API 500 errors` |
| `/explain` | Understand code | `/explain how auth works` |
| `/design` | Plan architecture | `/design caching layer` |
| `/analyze` | Code analysis | `/analyze performance issues` |
| `/brainstorm` | Generate ideas | `/brainstorm optimization strategies` |

---

### 🎯 Common Workflows

**Building a Feature:**
```
1. /research [technology]
2. /design [feature]
3. /pm implement [feature]
4. /test [feature]
```

**Debugging:**
```
1. /troubleshoot [error]
2. /analyze [problem area]
3. /pm fix [issue]
```

**Understanding Code:**
```
1. /index-repo (first time only)
2. /explain [what you want to know]
```

---

## 🔧 MCP SERVERS (Already Installed)

Your AI has these superpowers enabled:

| Server | What It Does | Status |
|--------|--------------|--------|
| **context7-sse** | Official documentation lookup | ✓ Connected |
| **sequential-thinking** | 30-50% token reduction | ✓ Connected |
| **serena** | Session persistence | ✓ Connected |
| **firecrawl** | Web scraping | ✗ Not working |
| **playwright** | Browser automation | ✗ Not working |

These work automatically - you don't need to do anything!

---

## 💡 QUICK START

### First Time Setup (Already Done!)
- ✅ SuperClaude installed
- ✅ MCP servers configured
- ✅ Docker service shortcuts created

### Your Daily Workflow

**1. Start Services (if needed):**
```bash
archon-start
mindbase-start
```

**2. Work on Your Project:**
```bash
cd ~/your-project
```

**3. Use SuperClaude:**
```
/pm [what you want to build]
```

**4. End of Day (optional):**
```bash
archon-stop
mindbase-stop
```

---

## 🎮 TRY IT NOW

### Test SuperClaude:
```
/explain what is the PM Agent pattern?
```

### Test Docker Services:
```bash
# From any directory:
archon-status
mindbase-status
```

### Real Work:
```
/pm create a simple hello world API endpoint
```

---

## 🆘 TROUBLESHOOTING

### "Command not found" for archon-start/mindbase-start:
```bash
source ~/.zshrc
```

### Docker service won't start:
```bash
# Make sure Docker Desktop is running first!
# Check System Tray/Menu Bar for Docker icon
```

### SuperClaude commands not showing:
- Restart Claude Code
- Check: `ls ~/.claude/commands/sc/`

### Check what Docker services are running:
```bash
docker ps
```

---

## 📍 LOCATIONS

| What | Where |
|------|-------|
| Archon repo | `/dev/archon` |
| Mindbase repo | `~/github/mindbase` |
| SuperClaude commands | `~/.claude/commands/sc/` |
| Shell config | `~/.zshrc` |
| This cheat sheet | `~/Desktop/CHEAT-SHEET.md` |

---

## 🧠 MENTAL MODELS

### Docker Services:
```
archon-start = Opening Spotify
archon-stop = Quitting Spotify
(You don't keep the installer folder open!)
```

### SuperClaude /pm:
```
Regular Claude: Starts coding immediately (might be wrong)
/pm Claude: Checks confidence first, researches, then codes (usually right)
```

### MCP Servers:
```
Like plugins for Claude - give it superpowers
Work automatically in the background
You don't interact with them directly
```

---

## ⚡ TERMINAL POWER SHORTCUTS

### Git Workflows (Daily Use)

| Command | What It Does | When to Use |
|---------|-------------|-------------|
| `commit "message"` | Add all files + commit | After making changes you want to save |
| `push` | Push to remote | After committing (share your work) |
| `pull` | Pull from remote | Start of day, before coding |
| `status` | See what changed | When you forget what you did |
| `save` | Auto-commit + push everything | End of day quick save |
| `undo` | Undo last commit (keep changes) | "Oops, wrong commit message" |

**Daily pattern:** `pull` → work → `commit "did stuff"` → `push`

---

### Project Maintenance (When Things Are Broken)

| Command | What It Does | When to Use |
|---------|-------------|-------------|
| `update` | Update packages + fix vulnerabilities | Weekly maintenance |
| `upgrade` | Pull latest code + install deps | After pulling from team |
| `fresh` | Nuke and reinstall node_modules | "Nothing works, idk why" |
| `install` | Install dependencies | After cloning a project |

**When shit breaks:** Try `fresh` first. Fixes 80% of problems.

---

### Development Shortcuts

| Command | What It Does | When to Use |
|---------|-------------|-------------|
| `dev` | Start dev server | Every time you start coding |
| `build` | Build for production | Before deploying |
| `test` | Run tests | Before pushing code |
| `check` | Lint + type check | Before committing |
| `fix` | Auto-fix lint errors | After `check` shows errors |

**Before pushing code:** `check` → `fix` → `test` → `commit`

---

### Diagnostic Tools (See What's Wrong)

| Command | What It Does | When to Use |
|---------|-------------|-------------|
| `ports` | See what's using ports | "Port 3000 already in use" |
| `processes` | See running node processes | Multiple servers running? |
| `diskspace` | See what's eating disk space | Running out of space |
| `see-containers` | List all Docker containers | Check what's running |

---

### Panic Buttons (When Everything Is On Fire)

| Command | What It Does | When to Use |
|---------|-------------|-------------|
| `killnode` | Kill ALL node processes | Server won't stop |
| `killport` | Kill process on port 3000 | Port stuck/won't free up |
| `restart` | Kill node + restart dev | "Just make it work again" |
| `docker-clean` | Stop containers + cleanup | Docker eating all RAM |
| `kill-containers` | Stop all Docker containers | Too many containers running |

**Nuclear option order:** `restart` → `killnode` → `fresh` → `docker-clean`

---

### How Often Should You Use These?

**Every Day:**
- `pull` (morning)
- `dev` (start coding)
- `commit "message"` (after each feature/fix)
- `push` (end of day or after major changes)

**Every Week:**
- `update` (keep packages current)
- `check` (before pushing)

**When Things Break:**
- `status` (what changed?)
- `fresh` (most common fix)
- `killnode` (server won't stop)
- `restart` (just make it work)

**Once Per Project:**
- `install` (after cloning)

---

## 🎯 THE ESSENTIALS (If You Only Remember 3 Things)

1. **`archon-start`** - Run from anywhere, starts Archon in background
2. **`/pm [task]`** - Use in Claude Code for any coding work
3. **`docker ps`** - See what's running

Everything else is just details.

---

## 📚 FULL DOCUMENTATION

- SuperClaude guide: `~/superclaude-quick-start.md`
- Docker services guide: `~/docker-services-help.md`
- SuperClaude repo: `~/SuperClaude_Framework/docs/`

---

**Last Updated:** 2025-11-22
**Your Setup:** macOS, zsh shell, SuperClaude v4.1.9

---

# QUICK REFERENCE TABLE

## Docker & Services
| Want to... | Command |
|-----------|---------|
| Start Archon | `archon-start` |
| Start Mindbase | `mindbase-start` |
| Check if services running | `docker ps` or `see-containers` |
| Stop services | `archon-stop` / `mindbase-stop` |
| Clean up Docker mess | `docker-clean` |

## Git & Code Management
| Want to... | Command |
|-----------|---------|
| Save my changes | `commit "what I did"` |
| Share my work | `push` |
| Get latest code | `pull` |
| Quick end-of-day save | `save` |
| See what I changed | `status` |
| Undo last commit | `undo` |

## Development
| Want to... | Command |
|-----------|---------|
| Start dev server | `dev` |
| Run tests | `test` |
| Build for production | `build` |
| Fix broken packages | `fresh` |
| Update packages | `update` |
| Check for errors | `check` |

## When Things Break
| Want to... | Command |
|-----------|---------|
| Kill stuck server | `killnode` |
| Free up a port | `killport` |
| See what's using ports | `ports` |
| Just make it work | `restart` |
| Nuclear option | `fresh` |

## Claude Code (SuperClaude)
| Want to... | Command |
|-----------|---------|
| Build a feature | `/pm implement [feature]` |
| Research something | `/research [topic]` |
| Debug an error | `/troubleshoot [error]` |
| Understand code | `/explain [what]` |
| Index a project | `/index-repo` |
| Generate tests | `/test [what]` |

---

**🎯 TL;DR:**
- **Morning:** `pull` → `archon-start` → `dev`
- **Working:** `/pm [task]` in Claude Code
- **End of day:** `commit "message"` → `push`
- **When broken:** `fresh` fixes 80% of problems
- Services run in background, close terminals freely!
