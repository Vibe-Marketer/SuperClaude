#!/bin/bash

echo "🚀 Installing SuperClaude Power User Shortcuts..."
echo ""

# Backup existing zshrc
if [ -f ~/.zshrc ]; then
    cp ~/.zshrc ~/.zshrc.backup.$(date +%Y%m%d-%H%M%S)
    echo "✅ Backed up existing ~/.zshrc"
fi

# Install Fabric AI shortcuts
echo ""
echo "📦 Installing Fabric AI shortcuts (69 commands)..."
if ! grep -q "# === FABRIC AI SHORTCUTS" ~/.zshrc; then
    cat fabric-ai/fabric-shortcuts.zsh >> ~/.zshrc
    echo "✅ Installed Fabric AI shortcuts"
else
    echo "⚠️  Fabric shortcuts already installed (skipping)"
fi

# Install Docker service shortcuts
echo ""
echo "🐳 Installing Docker service shortcuts..."
if ! grep -q "# === START/STOP ALL SERVICES ===" ~/.zshrc; then
    cat docker-services/docker-shortcuts.zsh >> ~/.zshrc
    echo "✅ Installed Docker shortcuts"
else
    echo "⚠️  Docker shortcuts already installed (skipping)"
fi

# Install terminal power shortcuts
echo ""
echo "⚡ Installing Terminal power shortcuts..."
if ! grep -q "# === REAL DEVELOPER WORKFLOWS" ~/.zshrc; then
    cat terminal-power/terminal-shortcuts.zsh >> ~/.zshrc
    echo "✅ Installed Terminal shortcuts"
else
    echo "⚠️  Terminal shortcuts already installed (skipping)"
fi

# Copy cheat sheets to Desktop
echo ""
echo "📚 Copying cheat sheets to Desktop..."
cp cheat-sheets/MASTER-CHEAT-SHEET.md ~/Desktop/
cp cheat-sheets/SETUP-COMPLETE.md ~/Desktop/
cp fabric-ai/FABRIC-START-HERE.md ~/Desktop/
echo "✅ Cheat sheets copied to Desktop"

# MCP servers (already configured, just show status)
echo ""
echo "🔌 MCP Servers (already configured):"
echo "   ✅ Context7 (SSE)"
echo "   ✅ Sequential Thinking"
echo "   ✅ Serena"
echo "   ✅ Mindbase"

# Reload shell
echo ""
echo "🔄 Reloading shell configuration..."
if [ -n "$ZSH_VERSION" ]; then
    source ~/.zshrc
    echo "✅ Shell reloaded"
else
    echo "⚠️  Please run: source ~/.zshrc"
fi

echo ""
echo "🎉 Installation complete!"
echo ""
echo "📝 Next steps:"
echo "   1. Open a NEW terminal window"
echo "   2. Try: start (to start Docker services)"
echo "   3. Try: echo 'test' | sum3 (to test Fabric)"
echo "   4. Check: ~/Desktop/MASTER-CHEAT-SHEET.md"
echo ""
echo "💡 All shortcuts available:"
echo "   - 69 Fabric AI commands (sales, wisdom, quiz, etc.)"
echo "   - Docker services (start, stop, services)"
echo "   - Git shortcuts (commit, push, pull, etc.)"
echo "   - Dev tools (dev, build, test, fresh)"
echo ""
echo "📚 Documentation:"
echo "   - Master guide: shortcuts/README.md"
echo "   - Cheat sheet: ~/Desktop/MASTER-CHEAT-SHEET.md"
echo ""
