# 🧵 FABRIC QUICK START GUIDE

Fabric = AI-powered text processing patterns. Think of it like AI shortcuts for common tasks.

---

## 🎯 HOW IT WORKS

```bash
# Basic format:
echo "your text" | fabric --pattern pattern-name

# Or from a file:
fabric --pattern pattern-name < file.txt

# Or copy to clipboard:
echo "text" | fabric --pattern pattern-name --copy
```

---

## 🔥 MOST USEFUL PATTERNS

### 📝 Writing & Content

| Pattern | What It Does | Example |
|---------|-------------|---------|
| `summarize` | Summarize text | `cat article.txt \| fabric -p summarize` |
| `create_summary` | Create detailed summary | `cat doc.md \| fabric -p create_summary` |
| `improve_writing` | Make writing better | `echo "my text" \| fabric -p improve_writing` |
| `extract_wisdom` | Pull key insights | `cat book.txt \| fabric -p extract_wisdom` |
| `write_essay` | Generate essay | `echo "topic" \| fabric -p write_essay` |

### 💻 Code & Tech

| Pattern | What It Does | Example |
|---------|-------------|---------|
| `explain_code` | Explain what code does | `cat script.py \| fabric -p explain_code` |
| `improve_code` | Make code better | `cat app.js \| fabric -p improve_code` |
| `find_hidden_message` | Find hidden meanings | `cat output.txt \| fabric -p find_hidden_message` |
| `analyze_logs` | Analyze log files | `cat error.log \| fabric -p analyze_logs` |

### 🎬 YouTube & Videos

| Pattern | What It Does | Example |
|---------|-------------|---------|
| `extract_youtube_info` | Get video info | `echo "URL" \| fabric -p extract_youtube_info` |
| `summarize_video` | Video summary | Video URL → summary |
| `get_youtube_rss` | Get channel RSS | Channel URL → RSS feed |

### 📊 Analysis

| Pattern | What It Does | Example |
|---------|-------------|---------|
| `analyze_paper` | Analyze research paper | `cat paper.pdf \| fabric -p analyze_paper` |
| `analyze_mistakes` | Learn from errors | `cat failure.txt \| fabric -p analyze_mistakes` |
| `analyze_claims` | Fact-check claims | `echo "claim" \| fabric -p analyze_claims` |
| `rate_content` | Rate quality 1-10 | `cat content.txt \| fabric -p rate_content` |

### 🧠 Ideas & Brainstorming

| Pattern | What It Does | Example |
|---------|-------------|---------|
| `create_idea_compass` | Generate ideas | `echo "topic" \| fabric -p create_idea_compass` |
| `create_aphorisms` | Create wisdom quotes | `cat text.txt \| fabric -p create_aphorisms` |
| `improve_prompt` | Make AI prompts better | `echo "prompt" \| fabric -p improve_prompt` |

### 🔍 Research

| Pattern | What It Does | Example |
|---------|-------------|---------|
| `extract_article_wisdom` | Key points from article | `cat article.txt \| fabric -p extract_article_wisdom` |
| `extract_references` | Pull citations | `cat paper.txt \| fabric -p extract_references` |
| `extract_sponsors` | Find sponsors | `cat content.txt \| fabric -p extract_sponsors` |

---

## 🚀 REAL-WORLD EXAMPLES

### Summarize a Long Article
```bash
curl https://example.com/article | fabric -p summarize
```

### Improve Your Writing
```bash
cat my-draft.md | fabric -p improve_writing > improved.md
```

### Explain Code
```bash
cat complex-script.py | fabric -p explain_code
```

### Extract Key Points from Video
```bash
echo "https://youtube.com/watch?v=..." | fabric -p summarize_video
```

### Analyze Your Mistakes
```bash
echo "I failed at X because Y" | fabric -p analyze_mistakes
```

---

## ⚡ POWER SHORTCUTS (Added to your ~/.zshrc)

I created these shortcuts for you:

```bash
# Summarize
summarize-text "your text here"
summarize-file filename.txt

# Improve writing
improve-text "your text"
improve-file draft.md

# Explain code
explain-file script.py

# Extract wisdom
extract-wisdom-file article.txt

# Copy to clipboard
fabric-copy "pattern-name" "your text"
```

---

## 📋 COMMON WORKFLOWS

### 1. Research an Article
```bash
# Download article → summarize → extract wisdom
curl https://article.com/post | fabric -p summarize > summary.txt
cat summary.txt | fabric -p extract_wisdom
```

### 2. Improve Your Code
```bash
# Explain code → get improvements
cat app.js | fabric -p explain_code
cat app.js | fabric -p improve_code > app-improved.js
```

### 3. Learn from Failures
```bash
# Write what went wrong → analyze
echo "Project failed because..." | fabric -p analyze_mistakes
```

### 4. Process YouTube Videos
```bash
# Get video summary → extract key points
echo "https://youtube.com/..." | fabric -p summarize_video > summary.txt
cat summary.txt | fabric -p extract_wisdom
```

---

## 🎮 TRY IT NOW

### Test 1: Summarize Text
```bash
echo "This is a long story about how I learned to code. It took many years and lots of practice. Eventually I got good at it and now I teach others." | fabric -p summarize
```

### Test 2: Improve Writing
```bash
echo "i think that coding is good and stuff" | fabric -p improve_writing
```

### Test 3: List All Patterns
```bash
fabric -l
```

---

## 🔧 ADVANCED OPTIONS

### Change AI Model
```bash
fabric -p summarize -m gpt-4
```

### Copy to Clipboard
```bash
echo "text" | fabric -p summarize --copy
```

### Save to File
```bash
echo "text" | fabric -p summarize -o output.txt
```

### Set Temperature (Creativity)
```bash
echo "text" | fabric -p write_essay -t 0.9
```

---

## 📚 MOST USEFUL PATTERNS LIST

**Content Creation:**
- `summarize` - Quick summaries
- `extract_wisdom` - Key insights
- `improve_writing` - Better prose
- `write_essay` - Generate essays
- `create_summary` - Detailed summaries

**Code:**
- `explain_code` - What does this do?
- `improve_code` - Make it better
- `coding_master` - Advanced coding help

**Analysis:**
- `analyze_paper` - Research papers
- `analyze_claims` - Fact checking
- `analyze_mistakes` - Learn from errors
- `rate_content` - Quality rating

**YouTube/Media:**
- `summarize_video` - Video summaries
- `extract_youtube_info` - Channel info
- `get_youtube_rss` - RSS feeds

---

## 🆘 TROUBLESHOOTING

### "Pattern not found"
```bash
# Update patterns
fabric -U
```

### "No API key"
```bash
# Run setup
fabric -S
```

### See all available patterns
```bash
fabric -l
```

### See all models
```bash
fabric -L
```

---

## 💡 THE SIMPLE EXPLANATION

**What Fabric Does:**
- You give it text
- You tell it what pattern to use
- It processes with AI
- You get transformed output

**Think of patterns like:**
- **Photoshop filters** for text
- Each pattern = different transformation
- Input text → pattern → output text

---

## 🎯 QUICK REFERENCE

| Want to... | Command |
|-----------|---------|
| Summarize text | `echo "text" \| fabric -p summarize` |
| Improve writing | `echo "text" \| fabric -p improve_writing` |
| Explain code | `cat file.py \| fabric -p explain_code` |
| Extract wisdom | `cat article.txt \| fabric -p extract_wisdom` |
| List patterns | `fabric -l` |
| Update patterns | `fabric -U` |
| Setup Fabric | `fabric -S` |

---

## 🔗 INTEGRATION WITH OTHER TOOLS

### With YouTube-DL
```bash
youtube-dl --skip-download --write-auto-sub URL
cat subtitles.txt | fabric -p summarize_video
```

### With curl
```bash
curl https://blog.com/post | fabric -p summarize
```

### With your clipboard
```bash
pbpaste | fabric -p improve_writing | pbcopy
```

---

**TL;DR:**
- Fabric = AI text processing patterns
- Basic: `echo "text" | fabric -p pattern-name`
- Most useful: `summarize`, `improve_writing`, `explain_code`, `extract_wisdom`
- List all: `fabric -l`
- Update: `fabric -U`

---

**Last Updated:** 2025-11-22
**Installation:** ✅ Already installed at `/Users/Naegele/.local/bin/fabric`
