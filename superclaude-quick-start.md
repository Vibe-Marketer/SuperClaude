# SuperClaude Quick Start - The Cool Shit You Can Do

## What Just Got Installed?

31 powerful slash commands that make Claude Code way smarter. Here are the coolest ones:

---

## 🔥 The Most Useful Commands

### `/pm` - Project Manager Mode
**The coolest feature!** Makes Claude check itself BEFORE doing work to avoid wasting tokens.

```
/pm implement a user authentication system
```

What it does:
- ✅ Checks confidence (≥90% to proceed, asks questions if unsure)
- ✅ Looks up official docs (no guessing/hallucinating)
- ✅ Validates after implementation
- ✅ Saves 25-250x tokens by not doing wrong work

**Use this for ANY significant coding task!**

---

### `/research` - Deep Research
Does web research + official docs lookup before answering.

```
/research best practices for React Server Components
```

Uses MCP servers (Tavily, Context7) to get actual facts, not guesses.

---

### `/index-repo` - Repository Indexing
Creates a searchable index of your entire codebase (94% token reduction!).

```
/index-repo
```

Then ask questions like "where is authentication handled?" and get instant answers.

---

### `/implement` - Confidence-First Implementation
Like `/pm` but focused on implementation.

```
/implement add dark mode toggle to settings
```

- Checks confidence first
- Plans implementation
- Writes code with validation

---

### `/test` - Smart Testing
Generates and runs tests for your code.

```
/test my authentication module
```

---

### `/troubleshoot` - Debug Helper
Analyzes errors and suggests fixes.

```
/troubleshoot why is my API returning 500 errors?
```

---

### `/explain` - Code Explanation
Explains code in detail.

```
/explain how does the ReflexionPattern work?
```

---

### `/design` - Architecture Design
Plans system architecture before coding.

```
/design a caching layer for the API
```

---

### `/brainstorm` - Idea Generation
Generates ideas and approaches.

```
/brainstorm ways to improve page load performance
```

---

### `/analyze` - Code Analysis
Deep analysis of code quality, patterns, issues.

```
/analyze the authentication flow
```

---

## 🚀 Pro Tips

### 1. Use `/pm` for Important Work
```
/pm add user registration with email verification
```
This prevents Claude from going in the wrong direction.

### 2. Index Your Repos
```
/index-repo
```
Do this once per project. Makes all future questions WAY faster.

### 3. Chain Commands
```
/research Next.js 15 app router patterns
# Then after understanding:
/pm implement app router with server actions
```

### 4. Use `/reflect` After Errors
```
/reflect on the test failures
```
Makes Claude learn from mistakes.

---

## 🎯 Common Workflows

### Building a New Feature:
```bash
1. /research [technology/pattern]
2. /design [feature architecture]
3. /pm implement [feature]
4. /test [feature]
5. /reflect [on any issues]
```

### Debugging:
```bash
1. /troubleshoot [error description]
2. /analyze [problematic code area]
3. /pm fix [the issue]
```

### Understanding Code:
```bash
1. /index-repo (first time only)
2. /explain [code/pattern/module]
3. /analyze [specific concerns]
```

---

## 🧠 The Big Picture

SuperClaude adds three game-changing patterns:

1. **ConfidenceChecker**: Don't start work unless ≥90% confident
2. **SelfCheckProtocol**: Validate after implementation with evidence
3. **ReflexionPattern**: Learn from errors across sessions

These patterns prevent token waste and improve accuracy.

---

## 📊 Token Savings

- **Without SuperClaude**: 50,000 tokens to build feature (might be wrong)
- **With `/pm`**: 5,000 tokens (checks confidence first, gets it right)
- **ROI**: Spend 200 tokens checking, save 45,000 tokens

---

## ⚡ Quick Examples

### Example 1: Safe Implementation
```
/pm add pagination to the user list component
```
Claude will:
1. Check if it knows how (confidence check)
2. Look up official docs if needed
3. Ask clarifying questions if unsure
4. Implement only when confident
5. Validate the result

### Example 2: Deep Research
```
/research how to implement rate limiting in Next.js 15
```
Claude will search official docs + web and give you researched answer.

### Example 3: Code Understanding
```
/index-repo
# Then later:
Where is the authentication middleware?
How does error handling work in this codebase?
```

---

## 🎮 Try This Right Now

1. **In this SuperClaude repo**, try:
   ```
   /explain what is the PM Agent pattern?
   ```

2. **Index this repo**:
   ```
   /index-repo
   ```

3. **Ask a question**:
   ```
   How does the confidence checker work?
   ```

4. **Use PM mode for real work**:
   ```
   /pm [your actual task]
   ```

---

## 🔗 Learn More

- Full docs: `/Users/Naegele/SuperClaude_Framework/docs/`
- All commands: Type `/` in Claude Code to see the list
- Help: `/help` for detailed command info

---

## TL;DR

**Just use `/pm` before any coding task.** It's like having a senior developer review the approach before writing code. Saves massive amounts of tokens and prevents wrong directions.

**Example:**
```
/pm build a REST API for user management
```

That's it. Claude will figure out the rest with confidence checks, research, and validation.
