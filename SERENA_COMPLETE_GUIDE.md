# Serena Complete Guide: Your AI Code Assistant's Memory

## 🎯 What is Serena? (In Plain English)

**Serena** is like giving your AI assistant a **notebook and understanding of your code**.

### The Simple Explanation

Imagine you're explaining your codebase to a new developer:
- **Without Serena**: They have to read every file from scratch each time
- **With Serena**: They have notes about your code structure, can instantly find functions, and remember what you discussed last session

**Serena does 3 main things:**
1. **Understands your code** (knows where functions are, how files connect)
2. **Remembers conversations** (saves session notes between chats)
3. **Helps navigate** (finds symbols, tracks dependencies)

---

## 🤔 Why Would You Use Serena?

### Real-World Scenarios

#### Scenario 1: Coming Back to a Project
**Without Serena:**
```
You (after 2 weeks): "What was I working on?"
AI: "I don't have context from before..."
You: *spend 30 minutes explaining everything again*
```

**With Serena:**
```
You (after 2 weeks): "What was I working on?"
AI: *reads Serena memory*
    "You were refactoring the authentication system. 
     You completed OAuth2 integration and were about 
     to add refresh token logic. The main blocker was 
     handling token expiration edge cases."
You: "Perfect, let's continue!"
```

#### Scenario 2: Large Codebase Navigation
**Without Serena:**
```
You: "Find all places where UserService is called"
AI: *searches through 100 files manually*
    "This might take a while..."
```

**With Serena:**
```
You: "Find all places where UserService is called"
AI: *uses Serena's symbol tracking*
    "Found 15 usages across 8 files:
     - AuthController.ts (3 calls)
     - ProfileService.ts (5 calls)
     ..."
```

#### Scenario 3: Refactoring
**Without Serena:**
```
You: "Rename getUserData to fetchUserProfile everywhere"
AI: "I'll do text search and replace..."
*Accidentally breaks things because it missed some references*
```

**With Serena:**
```
You: "Rename getUserData to fetchUserProfile everywhere"
AI: *uses Serena's semantic understanding*
    "I'll rename the function and update all 23 references,
     including type definitions and JSDoc comments."
*Does it correctly because Serena understands the code structure*
```

---

## 🛠️ How Serena Works

### The Technology

```
┌─────────────────────────────────────────┐
│        Your Codebase                     │
│  - 1000 files                            │
│  - Multiple languages                    │
│  - Complex dependencies                  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│         Serena MCP Server                │
│  - Analyzes code with LSP               │
│  - Builds symbol index                   │
│  - Tracks dependencies                   │
│  - Stores memory in .serena/            │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│      .serena/ Directory                  │
│  ├── memories/                          │
│  │   ├── session_2025-11-23.md        │
│  │   ├── architecture_notes.md        │
│  │   └── next_actions.md              │
│  └── symbols/                          │
│      └── project_index.db             │
└─────────────────────────────────────────┘
```

### What Serena Knows About Your Code

1. **Symbols** - All functions, classes, variables
2. **Dependencies** - What imports what
3. **Structure** - File organization and relationships
4. **History** - What you've discussed in past sessions

---

## 📚 Serena's Main Features

### 1. Memory Management

**Save conversations between sessions:**

```bash
# End of session
"Save my progress: We implemented JWT auth, 
 completed login endpoint, still need to add 
 refresh token logic"

# Next session (new conversation)
"What was I working on last time?"
# Serena retrieves saved memory automatically
```

**Commands:**
- `write_memory(name, content)` - Save notes
- `read_memory(name)` - Read notes
- `list_memories()` - See all saved notes
- `delete_memory(name)` - Remove notes

### 2. Code Understanding

**Navigate code intelligently:**

```bash
# Find symbols
"Where is the UserService class defined?"
"Show me all methods in AuthController"

# Track dependencies
"What files import the config module?"
"Show me all places that call fetchUser()"

# Understand structure
"Explain the authentication flow"
"Show me how the API routes are organized"
```

### 3. Smart Refactoring

**Make changes that understand your code:**

```bash
# Rename safely
"Rename getUserData to fetchUserProfile across the entire project"

# Extract functions
"Extract this validation logic into a separate function"

# Move code
"Move these utility functions to a utils file"
```

### 4. Project Activation

**Work on multiple projects:**

```bash
# Switch to project
"Activate project /Users/Naegele/MyProject"

# Serena remembers:
# - Project structure
# - Past conversations about this project
# - Where you left off
```

---

## 🚀 Getting Started with Serena

### Prerequisites

Already done in your setup! ✅
- Serena is configured in `~/.warp/claude.json`
- Uses `uvx` (you have `uv` installed)
- No API key needed

### How to Use It (Practical Examples)

#### 1. Start a Session

Just work normally! Serena activates automatically when you:
- Navigate large codebases
- Ask about code structure
- Request refactoring
- Save/load sessions

#### 2. Save Your Progress (End of Session)

```bash
# Natural language - Serena understands
"Save my session: I was implementing user authentication. 
 Completed the login endpoint with JWT tokens. Next step 
 is to add refresh token rotation logic."

# Or more explicit
"Write to memory: Authentication implementation progress"
```

#### 3. Resume Work (New Session)

```bash
# Ask what you were doing
"What was I working on in my last session?"

# Or explicitly read memory
"Read memory: authentication progress"
```

#### 4. Navigate Code

```bash
# Find things
"Where is the User model defined?"
"Show me all API endpoints"
"Find all database queries"

# Understand relationships
"What files use the AuthService?"
"Show dependencies for the payment module"
```

#### 5. Refactor Safely

```bash
# Rename
"Rename validateUser to validateUserInput everywhere"

# Extract
"Extract this error handling into a separate function"

# Reorganize
"Move all validation functions to validators/"
```

---

## 💡 Best Practices

### ✅ DO

1. **End sessions with summaries**
   ```bash
   "Save session: Implemented X, working on Y, 
    blocked by Z. Next: solve Z then continue Y."
   ```

2. **Start sessions by loading context**
   ```bash
   "What was I working on?"
   # Let Serena load the context
   ```

3. **Use for large projects**
   - 50+ files
   - Multiple languages
   - Complex architecture

4. **Let it learn your codebase**
   ```bash
   "Analyze this project structure"
   # Serena builds understanding
   ```

5. **Use for refactoring**
   - Safer than manual search-replace
   - Understands code semantics
   - Tracks all references

### ❌ DON'T

1. **Don't use for tiny scripts**
   - Single files don't need Serena
   - Overhead not worth it

2. **Don't expect mind-reading**
   - Be explicit about what to save
   - Tell it when to load context

3. **Don't store sensitive data**
   - Memories are in `.serena/` folder
   - Don't save API keys or passwords

4. **Don't forget to save**
   - End sessions with summaries
   - Otherwise context is lost

---

## 🎯 When to Use Serena vs Other Tools

### Use Serena When:
- ✅ Navigating large codebases (50+ files)
- ✅ Refactoring across multiple files
- ✅ Need to remember context between sessions
- ✅ Want semantic code understanding
- ✅ Working on long-term projects

### Don't Use Serena When:
- ❌ Single file, simple edits
- ❌ One-off scripts
- ❌ Just starting a project (< 10 files)
- ❌ Don't need session persistence

### Serena vs Other MCPs

| Task | Use This |
|------|----------|
| Remember conversations across ALL projects | Mindbase |
| Remember this project's session | Serena |
| Find official documentation | context7 |
| Complex debugging | sequential-thinking |
| Browser testing | playwright |
| Web search | tavily |

---

## 📂 Where Does Serena Store Things?

### In Your Project

```
YourProject/
├── .serena/              # Serena's data
│   ├── memories/         # Session notes
│   │   ├── last_session.md
│   │   ├── architecture.md
│   │   └── progress.md
│   └── symbols/          # Code index
│       └── index.db
├── .gitignore           # Add .serena/ here!
└── your code...
```

**Important:** Add `.serena/` to `.gitignore`:
```bash
# Add to .gitignore
.serena/
```

---

## 🔧 Troubleshooting

### Serena Not Working?

1. **Check if it's configured**
   ```bash
   cat ~/.warp/claude.json | grep serena
   ```
   Should show serena configuration.

2. **Restart Warp**
   Quit and reopen Warp completely.

3. **Check uv is installed**
   ```bash
   uv --version
   ```
   Should show version (you have this).

4. **Try explicitly**
   ```bash
   "List my Serena memories"
   ```
   If it responds, Serena is working.

### Common Issues

**"I don't see my saved session"**
- Make sure you saved with: "Save my progress: ..."
- Try: "List memories" to see what's saved

**"Serena can't find my code"**
- Make sure you're in the project directory
- Try: "Activate project /path/to/project"

**"Changes broke something"**
- Serena needs to understand your code first
- Let it analyze the project before big changes

---

## 🎓 Quick Examples

### Example 1: End of Day Save

```bash
You: "Save today's work: Finished user authentication 
      endpoints. All tests passing. Tomorrow: implement 
      password reset flow using email service. Main 
      blocker: need SMTP credentials from DevOps."

AI: "Saved to memory. I'll remember this for next session."
```

### Example 2: Next Day Resume

```bash
You: "What did I work on yesterday?"

AI: "Yesterday you finished user authentication endpoints 
     with passing tests. You were planning to implement 
     password reset using email service, but were blocked 
     waiting for SMTP credentials from DevOps. Would you 
     like to continue with password reset or work on 
     something else while waiting?"
```

### Example 3: Code Navigation

```bash
You: "Find all files that import UserService"

AI: *uses Serena*
    "Found 8 files importing UserService:
     1. auth/AuthController.ts
     2. api/UserRouter.ts
     3. middleware/AuthMiddleware.ts
     4. services/ProfileService.ts
     5. tests/auth.test.ts
     ..."
```

### Example 4: Safe Refactoring

```bash
You: "Rename isValidEmail to validateEmailFormat in 
      all files"

AI: *uses Serena's semantic understanding*
    "I'll rename the function and update 15 references 
     across 6 files:
     - utils/validators.ts (definition)
     - auth/SignupController.ts (2 calls)
     - services/EmailService.ts (1 call)
     ...
     Would you like me to proceed?"
```

---

## 📊 Summary

**Serena = Your Project's Memory & Code Guide**

| Feature | Benefit |
|---------|---------|
| **Saves sessions** | Resume work after breaks |
| **Understands code** | Navigate large projects |
| **Tracks symbols** | Find anything instantly |
| **Smart refactoring** | Rename/move safely |
| **Project memory** | Remembers discussions |

**You already have it configured! ✅**

Just start using natural language:
- "Save my progress: ..."
- "What was I working on?"
- "Find all uses of X"
- "Rename Y to Z everywhere"

Serena will activate automatically when needed! 🚀

---

## 🆚 Quick Comparison: Serena vs Mindbase

**Serena** = Project notebook
- Saves notes about current project
- Understands code structure
- Works per-project

**Mindbase** = Personal library  
- Searches ALL past conversations
- Works across ALL projects
- Semantic search everything

**Use Serena for**: Day-to-day project work
**Use Mindbase for**: Cross-project knowledge discovery

**Current setup**: You have Serena ✅, Mindbase is optional
