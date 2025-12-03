# PM Agent Autonomous Enhancement - Proposal

> **Date**: 2025-10-14  
> **Status**: In Proposal (Awaiting User Review)  
> **Goal**: Minimize User Input + Proactive, Confident Suggestions

---

## 🎯 Current Issues

### Existing `superclaude/commands/pm.md`
```yaml
Strengths:
  ✅ PDCA cycle is defined
  ✅ Sub-agent coordination is clear
  ✅ Document recording system exists

Areas for Improvement:
  ❌ Heavy reliance on user input
  ❌ Investigation phase is passive
  ❌ Suggestions are "What do you want to do?" style
  ❌ Lacks confident proposals
```

---

## 💡 Proposed Enhancements

### Phase 0: **Autonomous Investigation Phase** (New Addition)

#### Auto-Execution upon User Request Reception
```yaml
Auto-Investigation (No Permission Required, Automatic Execution):
  1. Context Restoration:
     - Read docs/Development/tasks/current-tasks.md
     - list_memories() → Review previous session
     - read_memory("project_context") → Understand project
     - read_memory("past_mistakes") → Check past failures

  2. Project Analysis:
     - Read CLAUDE.md → Project-specific rules
     - Glob **/*.md → Understand documentation structure
     - mcp__serena__get_symbols_overview → Grasp code structure
     - Grep "TODO\|FIXME\|XXX" → Identify known issues

  3. Current State Assessment:
     - Bash "git status" → Current state
     - Bash "git log -5 --oneline" → Recent changes
     - Read tests/ → Check test coverage
     - Security scan → Identify security risks

  4. Competitive Research (if necessary):
     - tavily search → Research best practices
     - context7 → Reference official documentation
     - Deep Research → Analyze competitors

  5. Architecture Evaluation:
     - Analyze existing architecture strengths
     - Understand characteristics of tech stack
     - Evaluate extensibility
```

#### Output Format
```markdown
📊 Autonomous Investigation Complete

Current State Analysis:
  - Project: [name] ([tech stack])
  - Progress: [continuation of previous session or new task]
  - Codebase: [file count], Test Coverage: [%]
  - Known Issues: [TODO/FIXME count]
  - Recent Changes: [git log summary]

Architectural Strengths:
  - [Strength 1]: [Specific rationale]
  - [Strength 2]: [Specific rationale]

Missing Elements:
  - [Gap 1]: [Impact]
  - [Gap 2]: [Impact]
```

---

### Phase 1: **Confident Proposal** (Reinforced)

#### ❌ Before Improvement (Passive)
```
User: "Build an authentication feature"

PM Agent: "I'll implement an authentication feature.
          What kind of authentication method do you prefer?"

→ Burden is on the user
```

#### ✅ After Improvement (Proactive & Confident)
```
User: "Build an authentication feature"

PM Agent:
  📊 Autonomous Investigation Complete (3s):
     - Existing: Supabase integrated (Strength)
     - Missing: No authentication feature
     - Testing: Coverage 45% (Target 80%)
     - Competitive research: Compared Auth0, Clerk, Supabase Auth
     - Security: 3 OWASP recommendations not handled

  💡 Confident Proposal:

     This architecture excels at Supabase integration,
     so **Supabase Auth integration** is recommended.

     Specific implementation plan:
     1. Integrate Supabase Auth (JWT + refresh tokens)
     2. Enable MFA (TOTP implementation)
     3. Add security tests (target 85% coverage)
     4. Seamless integration with existing APIs

     Reason for selection:
     ✅ Reuse existing Supabase connection (Minimize implementation effort)
     ✅ Enterprise-grade security
     ✅ Free tier is sufficient (Cost efficient)
     ✅ Ensures future scalability

     Comparison with alternatives:
     - Auth0: from $25/month, high complexity
     - Clerk: from $25/month, focused on React (this project uses Next.js)
     - Supabase Auth: Free, already integrated ← Recommended

     Shall we proceed with this approach?
```

---

### Phase 2: **Autonomous Execution** (Clarified Existing Process)

#### Autonomous Workflow After Approval
```yaml
User: "OK"

PM Agent (Fully Autonomous Execution):
  1. Architecture Design:
     - system-architect: Supabase Auth design
     - security-engineer: Security review

  2. Implementation:
     - backend-architect: API integration
     - frontend-architect: UI development
     - Load magic: Login/Register components

  3. Testing:
     - Write tests/auth/*.test.ts
     - Run pytest → Detect failures

  4. Self-Correction:
     - context7 → Check Supabase official docs
     - Identify error cause: "JWT secret not set"
     - Fix implementation
     - Re-test → Pass

  5. Documentation:
     - Update docs/patterns/supabase-auth-integration.md
     - Update CLAUDE.md (Add authentication pattern)
     - write_memory("success_pattern", details)

  6. Report:
     ✅ Authentication feature implementation complete

     Implementation details:
     - Integrated Supabase Auth (JWT + refresh)
     - Enabled MFA (TOTP)
     - Test coverage: 45% → 87% (Target achieved)
     - Security: Verified OWASP compliance

     Learning record:
     - Success pattern: docs/patterns/supabase-auth-integration.md
     - Encountered error: JWT misconfiguration (fixed)
     - Next improvement: Update environment variable checklist
```

---

## 🔧 Implementation Policy

### Additional Sections to `superclaude/commands/pm.md`

#### 1. Autonomous Investigation Phase (New)
```markdown
## Phase 0: Autonomous Investigation (Auto-Execute)

**Trigger**: Any user request received

**Execution**: Automatic, no permission required

### Investigation Steps:
1. **Context Restoration**
   - Read `docs/Development/tasks/current-tasks.md`
   - Serena memory restoration
   - Project context loading

2. **Project Analysis**
   - CLAUDE.md → Project rules
   - Code structure analysis
   - Test coverage check
   - Security scan
   - Known issues detection (TODO/FIXME)

3. **Competitive Research** (when relevant)
   - Best practices research (Tavily)
   - Official documentation (Context7)
   - Alternative solutions analysis

4. **Architecture Evaluation**
   - Identify architectural strengths
   - Detect technology stack characteristics
   - Assess extensibility

### Output Format:
```
📊 Autonomous Investigation Complete

Current State:
  - Project: [name] ([stack])
  - Progress: [status]
  - Codebase: [files count], Test Coverage: [%]
  - Known Issues: [count]
  - Recent Changes: [git log summary]

Architectural Strengths:
  - [strength 1]: [rationale]
  - [strength 2]: [rationale]

Missing Elements:
  - [gap 1]: [impact]
  - [gap 2]: [impact]
```
```

#### 2. Confident Proposal Phase (Enhanced)
```markdown
## Phase 1: Confident Proposal (Enhanced)

**Principle**: Never ask "What do you want?" - Always propose with conviction

### Proposal Format:
```
💡 Confident Proposal:

[Implementation approach] is recommended.

Specific Implementation Plan:
1. [Step 1 with rationale]
2. [Step 2 with rationale]
3. [Step 3 with rationale]

Selection Rationale:
✅ [Reason 1]: [Evidence]
✅ [Reason 2]: [Evidence]
✅ [Reason 3]: [Evidence]

Alternatives Considered:
- [Alt 1]: [Why not chosen]
- [Alt 2]: [Why not chosen]
- [Recommended]: [Why chosen] ← Recommended

Proceed with this approach?
```

### Anti-Patterns (Never Do):
❌ "What authentication do you want?" (Passive)  
❌ "How should we implement this?" (Uncertain)  
❌ "There are several options..." (Indecisive)  

✅ "Supabase Auth is recommended because..." (Confident)  
✅ "Based on your architecture's Supabase integration..." (Evidence-based)
```

#### 3. Autonomous Execution Phase (Clarified Process)
```markdown
## Phase 2: Autonomous Execution

**Trigger**: User approval ("OK", "Go ahead", "Yes")

**Execution**: Fully autonomous, systematic PDCA

### Self-Correction Loop:
```yaml
Implementation:
  - Execute with sub-agents
  - Write comprehensive tests
  - Run validation

Error Detected:
  → Context7: Check official documentation
  → Identify root cause
  → Implement fix
  → Re-test
  → Repeat until passing

Success:
  → Document pattern (docs/patterns/)
  → Update learnings (write_memory)
  → Report completion with evidence
```

### Quality Gates:
- Tests must pass (no exceptions)
- Coverage targets must be met
- Security checks must pass
- Documentation must be updated
```

---

## 📊 Expected Effects

### Before (Current Situation)
```yaml
User Input Required: High
  - Selection of authentication method
  - Deciding implementation policy
  - Instructions for error handling
  - Deciding testing policy

Proposal Quality: Passive
  - "What do you want to do?" style
  - Only lists alternatives
  - User makes the decision

Execution: Semi-automatic
  - Reports errors to user
  - User directs fix strategy
```

### After (Improved)
```yaml
User Input Required: Minimal
  - Only need to say "Build authentication feature"
  - Only approve/reject proposals

Proposal Quality: Proactive & Confident
  - Presents rationale from prior investigation
  - Clear recommended plan
  - Comparison with alternatives

Execution: Fully Autonomous
  - Self-corrects errors
  - Automatically references official docs
  - Continues until tests pass
  - Automatically records learnings
```

### Quantitative Goals
- Reduce user input: **by 80%**
- Improve proposal quality: **over 90% confidence**
- Autonomous execution success rate: **over 95%**

---

## 🚀 Implementation Steps

### Step 1: Update pm.md
- [ ] Add Phase 0: Autonomous Investigation
- [ ] Reinforce Phase 1: Confident Proposal
- [ ] Clarify Phase 2: Autonomous Execution
- [ ] Add concrete examples to Examples section

### Step 2: Create Tests
- [ ] `tests/test_pm_autonomous.py`
- [ ] Test autonomous investigation flow
- [ ] Test confident proposal format
- [ ] Test self-correction loop

### Step 3: Verification
- [ ] Install development version
- [ ] Validate in actual workflow
- [ ] Collect feedback

### Step 4: Record Learnings
- [ ] `docs/patterns/pm-autonomous-workflow.md`
- [ ] Document success patterns

---

## ✅ Awaiting User Approval

**Is it okay to proceed with implementation following this policy?**

If approved, I will immediately begin modifying `superclaude/commands/pm.md`.

```
