# 🐳 Docker Services - Start/Stop Simplification

One command to rule them all.

---

## 💡 The Big Idea

**Instead of this:**
```bash
# Navigate to Archon
cd /dev/archon
docker compose up -d
# Keep terminal open...

# Navigate to Mindbase
cd ~/github/mindbase
docker compose up -d
# Keep another terminal open...

# Remember what's running where...
# Try to stop them later...
```

**Do this:**
```bash
start
```

---

## 🎯 What You Get

**Three simple commands:**
- `start` - Start all services (Archon + Mindbase)
- `stop` - Stop all services
- `services` - See what's running

**No more:**
- ❌ Navigating to repo directories
- ❌ Remembering docker compose commands
- ❌ Keeping terminals open
- ❌ Forgetting what's running

**Instead:**
- ✅ Type `start` from anywhere
- ✅ Close all terminals
- ✅ Work on anything
- ✅ Services run in background

---

## 🧠 Mental Model

Think of it like Spotify:

**Bad way (old):**
1. Find Spotify installer folder
2. Stay in that folder
3. Keep terminal open
4. Run complex command
5. Don't close the window!

**Good way (this):**
1. Type `start`
2. Close terminal
3. Use computer normally
4. Type `stop` when done

---

## ⚡ Installation

```bash
# Copy shortcuts to ~/.zshrc
cat docker-shortcuts.zsh >> ~/.zshrc

# Reload
source ~/.zshrc

# Test
start
services
stop
```

---

## 💻 Usage

### Daily Workflow

**Morning:**
```bash
start
# ✅ All services started!
# Close terminal, do your work
```

**During Day:**
```bash
# Work on any project
# Services run in background
# No need to think about them
```

**Check Status:**
```bash
services
# See what's running
```

**End of Day (optional):**
```bash
stop
# ✅ All services stopped!
# Or just leave them running
```

---

## 🔧 What It Does

### The `start` Command
```bash
start
# 🚀 Starting all services...
# Starting Archon...
# Starting Mindbase...
# ✅ All services started!
```

**Behind the scenes:**
1. Navigates to `/dev/archon` → `make up`
2. Navigates to `~/github/mindbase` → `make up`
3. Returns you to your current directory
4. Services run in background

### The `stop` Command
```bash
stop
# 🛑 Stopping all services...
# Stopping Archon...
# Stopping Mindbase...
# ✅ All services stopped!
```

### The `services` Command
```bash
services
# NAMES                STATUS              PORTS
# archon-api          Up 2 hours         0.0.0.0:3000->3000/tcp
# mindbase-postgres   Up 2 hours         0.0.0.0:15434->5432/tcp
```

---

## 📚 Individual Service Commands

If you need to manage services individually:

**Archon:**
```bash
archon-start
archon-stop
archon-status
```

**Mindbase:**
```bash
mindbase-start
mindbase-stop
mindbase-status
```

---

## 🎯 Philosophy

### Abstract Infrastructure Away
Users shouldn't think about:
- Docker compose commands
- Service locations
- Port mappings
- Container names

They should think about:
- "I need services running" → `start`
- "Are they running?" → `services`
- "Stop everything" → `stop`

### Services as Utilities
Like electricity - flip the switch, it works, don't think about the power plant.

### Stateless Mental Model
Don't keep state in your head:
- "Did I start Mindbase?"
- "Which terminal is Archon in?"
- "Can I close this terminal?"

Just run `services` to see current state.

---

## 🛠️ Customization

### Add More Services

Edit `docker-shortcuts.zsh`:

```bash
# Add new service shortcuts
alias myservice-start='(cd ~/my-service && make up)'
alias myservice-stop='(cd ~/my-service && make down)'

# Update unified start/stop
alias start='echo "🚀 Starting all services..." && archon-start && mindbase-start && myservice-start && echo "✅ All services started!"'
alias stop='echo "🛑 Stopping all services..." && archon-stop && mindbase-stop && myservice-stop && echo "✅ All services stopped!"'
```

### Change Commands

Prefer different names?

```bash
alias up='start'
alias down='stop'
alias running='services'
```

---

## 💰 Impact

**Time Saved:**
- No fumbling with docker commands: 2-3 min/day
- No navigating to repos: 1 min/day
- No mental overhead: Priceless

**Cognitive Load:**
- Before: Remember paths, commands, state
- After: Remember 3 words

**Reliability:**
- Before: Forget to start services, stuff breaks
- After: Type `start`, everything works

---

## 📁 Files

- **docker-shortcuts.zsh** - All command definitions
- **README.md** - This file
- **MENTAL-MODEL.md** - Deep dive on the philosophy

---

## 🔄 Troubleshooting

**Services won't start:**
```bash
# Make sure Docker Desktop is running
# Check System Tray/Menu Bar for Docker icon
```

**"Command not found":**
```bash
source ~/.zshrc
```

**See what's actually running:**
```bash
docker ps
```

---

**Created:** 2025-11-22
**Services Managed:** Archon, Mindbase
**Commands:** 3 main (`start`, `stop`, `services`) + 6 individual
**Location:** `~/.zshrc`
