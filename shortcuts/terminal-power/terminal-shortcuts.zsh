# === REAL DEVELOPER WORKFLOWS (Full words you'll actually remember) ===

# Git workflows (the stuff you SHOULD be doing)
alias commit='git add . && git commit -m'
alias push='git push'
alias pull='git pull'
alias status='git status'
alias upgrade='git pull && npm install'
alias save='git add . && git commit -m "WIP" && git push'
alias undo='git reset --soft HEAD~1'

# Project setup/maintenance (stuff that takes forever)
alias fresh='rm -rf node_modules package-lock.json && npm install'
alias install='npm install'
alias update='npm update && npm audit fix'

# Check what's broken
alias check='npm run lint && npm run type-check'
alias fix='npm run lint -- --fix'

# See what's eating resources
alias ports='lsof -i -P -n | grep LISTEN'
alias processes='ps aux | grep node'
alias diskspace='du -sh * | sort -h'

# Docker management (instead of fighting with containers)
alias docker-clean='docker stop $(docker ps -aq) && docker system prune -af'
alias see-containers='docker ps -a'
alias kill-containers='docker stop $(docker ps -aq)'

# When shit breaks (the panic buttons)
alias killnode='killall -9 node'
alias killport='kill -9 $(lsof -ti:3000)'  # Change 3000 to whatever port
alias restart='killall -9 node && npm run dev'

# Project navigation (if you have common paths)
alias projects='cd ~/projects'
alias work='cd ~/work'


# === START/STOP ALL SERVICES ===
alias start='echo "🚀 Starting all services..." && archon-start && mindbase-start && echo "✅ All services started!"'
alias stop='echo "🛑 Stopping all services..." && archon-stop && mindbase-stop && echo "✅ All services stopped!"'
alias services='docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"'


# === FABRIC AI SHORTCUTS (Tiers 1 + 2) ===
# Added by Claude Code on 2025-11-22
# Usage: cat file.txt | sales
# Or: sales < file.txt
# Or with drag & drop: sales (then drag file into terminal)

# TIER 1: Daily Use (Must Have)
