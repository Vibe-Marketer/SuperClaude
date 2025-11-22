# 🧵 Fabric AI - Single Word Commands

Transform complex AI operations into single-word commands.

---

## 💡 The Big Idea

**Instead of this:**
```bash
cat long-sales-transcript.txt | fabric --pattern analyze_sales_call --output analysis.txt
```

**Do this:**
```bash
sales < transcript.txt
```

---

## 🎯 What You Get

**69 single-word shortcuts** that turn any text into:
- Sales analysis
- Coaching summaries
- Extracted wisdom
- Quiz questions
- Action items
- And 64 more...

---

## 🔥 Top 10 Commands

| Command | Use After | What You Get |
|---------|-----------|--------------|
| `sales` | Sales calls | Full analysis: techniques, objections, next steps |
| `session` | Coaching calls | Summary to email clients |
| `wisdom` | Any content | Key insights and takeaways |
| `hw` | Client sessions | Action items list |
| `sum3` | Anything long | Quick 2-3 paragraph summary |
| `quiz` | Course content | 10-15 quiz questions |
| `upsell` | Business content | Spot opportunities |
| `real` | Discovery calls | The REAL core problem |
| `deep` | Multiple calls | Find patterns and insights |
| `better` | Your drafts | Improved writing |

---

## 📊 All 69 Commands

### TIER 1 - Daily (9)
```
sales session wisdom hw sum3 quiz upsell real deep
```

### TIER 2 - Weekly (10)
```
better FAQs chapters lines5 hooks cards claims fail objections tone
```

### TIER 3 - Monthly (20)
```
compare debate present feedback ideas essay easycode books yt interview
mozi one-liner news blog keynote story email reading tweet mini-essay
```

### TIER 4 - Specialized (20)
```
risks props prose false hidden predict solution features partners sources
bettercode addcode newcode reviewcode designdoc prd git pr
```

### TIER 5 - Nice to Have (10)
```
article jokes characters recipe sing zoom paper lecture prompt trans
```

---

## ⚡ Installation

```bash
# Copy the shortcuts to your ~/.zshrc
cat fabric-shortcuts.zsh >> ~/.zshrc

# Reload your shell
source ~/.zshrc

# Test it works
echo "Test" | sum3
```

---

## 💻 Usage

### Three Ways to Use:

**1. Pipe from file:**
```bash
cat transcript.txt | sales
```

**2. Redirect input:**
```bash
sales < transcript.txt
```

**3. Drag & drop:**
```bash
# Type: sales
# Drag file from Finder into terminal
# Press Enter
```

---

## 🎨 Add Your Own

```bash
# See all available Fabric patterns
fabric -l

# Add custom shortcut
add mystuff extract_wisdom "My custom extractor"

# Use it
cat file.txt | mystuff
```

---

## 📚 Reference Files

- **fabric-shortcuts.zsh** - All 69 command definitions
- **COMPLETE-GUIDE.md** - Detailed guide for all commands
- **QUICK-REFERENCE.md** - Printable quick reference card
- **EXAMPLES.md** - Real-world usage examples

---

## 🚀 Real Examples

### After a Sales Call
```bash
sales < call.txt > analysis.txt
real < call.txt >> analysis.txt
upsell < call.txt >> analysis.txt
lines5 < call.txt > crm-note.txt
```

### Process Course Content
```bash
wisdom < lesson.txt > key-points.txt
quiz < lesson.txt > student-quiz.txt
cards < lesson.txt > flashcards.txt
```

### Batch Process Multiple Files
```bash
for file in *.txt; do
  sales < "$file" > "analysis-$file"
done
```

---

## 💰 Time Saved

- **Sales calls:** 29 min per call (30 min → 1 min)
- **Coaching follow-ups:** 14 min per session (15 min → 1 min)
- **Course materials:** ~4 hours per course (4h → 5 min)
- **Book summaries:** ~2 hours per book (2h → 1 min)

**Total: 6-10 hours saved per week**

---

## 🎯 Philosophy

### Single Word > Complex Command
Your brain should focus on the task, not the syntax.

**Bad:** Try to remember fabric command syntax
**Good:** Type one word that describes what you want

### Descriptive > Abbreviated
`sales` is better than `sc` because you'll remember it in 6 months.

### Consistent Patterns
- Analysis: `sales`, `session`, `debate`
- Extraction: `wisdom`, `hw`, `hooks`
- Creation: `quiz`, `cards`, `blog`
- Improvement: `better`, `claims`, `fail`

---

**Created:** 2025-11-22
**Commands:** 69 + `add` function for custom ones
**Location:** `~/.zshrc`
