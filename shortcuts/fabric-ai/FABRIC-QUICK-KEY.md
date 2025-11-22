# 🎯 FABRIC COMMAND QUICK KEY

Your 19 essential Fabric AI shortcuts - installed and ready to use!

---

## ⚡ HOW TO USE

### Three Ways to Use Any Command:

**1. Pipe from file:**
```bash
cat transcript.txt | sales
```

**2. Redirect input:**
```bash
sales < transcript.txt
```

**3. Drag & drop (easiest!):**
```bash
# Type the command, then drag file from Finder into terminal:
sales [drag file here]
```

---

## 🔥 TIER 1: DAILY USE (Must Have)

| Command | What You Get | Use After... |
|---------|--------------|--------------|
| `sales` | Sales techniques, objections, what worked/didn't work | Every sales call |
| `session` | Full summary perfect for emailing to clients | Coaching sessions |
| `wisdom` | Key takeaways, quotes, practical applications | Courses/books |
| `hw` | Action items and homework assignments | Client sessions |
| `sum3` | 2-3 paragraph summary of main points | Any long content |
| `quiz` | 10-15 quiz questions auto-generated | Course creation |
| `upsell` | Business ideas, product opportunities, pain points | Calls/content |
| `real` | The REAL core problem (not what they say) | Discovery calls |
| `deep` | Strategic insights and "aha moments" | Multiple calls |

---

## ⭐ TIER 2: WEEKLY USE (Very Useful)

| Command | What You Get | Use For... |
|---------|--------------|------------|
| `better` | Your writing but clearer and more persuasive | Content upgrade |
| `FAQs` | Every question asked in content | Building FAQs |
| `chapters` | Chapter titles + timestamps | Long videos/courses |
| `lines5` | Exactly 5 sentences | CRM notes |
| `hooks` | 10-20 attention-grabbing opening hooks | Content/offers |
| `cards` | Study flashcards (Q&A format) | Student materials |
| `claims` | Fact-check of claims made | Content accuracy |
| `fail` | What went wrong, why, how to avoid | Learn from mistakes |
| `objections` | All objections + how you handled them | Sales improvement |
| `tone` | Voice/tone/personality analysis | Brand voice |

---

## 🎬 REAL EXAMPLES YOU CAN RUN NOW

### After a Sales Call:
```bash
cd ~/Desktop/main/LEGENDS/[LEGENDS]\ JON\ BENSON/AICA/AICA\ Live\ Call\ Transcripts
sales < "AICA LIVE Individual Calls/9. AICA-Week8-Live-Call.txt"
```

### Extract Wisdom from RMBC2 Course:
```bash
cd ~/Downloads/RMBC2/md\ transcripts
wisdom < "01-Intro_01_Welcome_To_RMBC2_Course_Overview.md"
```

### Quick Summary of Any Book:
```bash
cd ~/Desktop/main
3p < "THE THIRD DOOR.md"
```

### After a Coaching Session:
```bash
session < call-transcript.txt > email-to-client.txt
hw < call-transcript.txt >> email-to-client.txt
```

---

## 💡 POWER WORKFLOWS

### Sales Call Complete Analysis:
```bash
# Get everything from one call:
cat call.txt | sales > analysis.txt
cat call.txt | real >> analysis.txt
cat call.txt | upsell >> analysis.txt
cat call.txt | 5lines > crm-note.txt
```

### Coaching Call Follow-Up:
```bash
# Email package for client:
cat call.txt | session > client-email.txt
cat call.txt | hw >> client-email.txt

# Your records:
cat call.txt | deep > insights.txt
```

### Course Material Creation:
```bash
# From one lesson, create everything:
cat lesson.txt | wisdom > key-points.txt
cat lesson.txt | quiz > student-quiz.txt
cat lesson.txt | cards > flashcards.txt
cat lesson.txt | chapters > outline.txt
```

### Batch Process Multiple Calls:
```bash
# Analyze ALL sales calls at once:
cd ~/Desktop/main/PROOF/Testimonials
for file in *.txt; do
  echo "=== $file ===" >> all-insights.txt
  cat "$file" | deep >> all-insights.txt
done
```

---

## 🚀 TRY IT RIGHT NOW

### Test #1: Quick Summary
```bash
echo "This is a long story about how I learned marketing from Dan Kennedy. It took many years of studying his materials and implementing his strategies. Eventually I got really good at direct response marketing and now I teach it to others through my RMBC2 course." | 3p
```

### Test #2: Improve Writing
```bash
echo "i think that marketing is good and stuff and you should do it" | better
```

### Test #3: Extract Wisdom (with your actual file)
```bash
wisdom < ~/Desktop/main/THE\ THIRD\ DOOR.md
```

---

## 📊 COMMAND FREQUENCY GUIDE

**Every Day (After Each):**
- `sales` - Every sales call
- `session` - Every coaching session
- `hw` - Every client session
- `lines5` - CRM notes

**2-3x Per Week:**
- `wisdom` - Processing courses/books
- `quiz` - Course creation
- `deep` - Finding patterns
- `upsell` - Spot opportunities

**Weekly:**
- `better` - Content creation
- `FAQs` - Documentation
- `chapters` - Video organization
- `hooks` - Marketing content

**As Needed:**
- `real` - Discovery calls
- `fail` - Post-mortems
- `claims` - Fact-checking
- `objections` - Sales training
- `tone` - Brand analysis
- `cards` - Student materials

---

## 🎯 THE ESSENTIALS (Remember These 5)

1. **`sales`** - After sales calls (most valuable)
2. **`session`** - After coaching (send to clients)
3. **`wisdom`** - From courses/books (your library!)
4. **`hw`** - Action items (follow-ups)
5. **`sum3`** - Quick summary (anything)

The other 14 are bonuses when you need them!

---

## 🆘 TROUBLESHOOTING

**"Command not found":**
```bash
source ~/.zshrc
```

**Fabric not working:**
```bash
# Check Fabric is installed:
which fabric

# Update patterns:
fabric -U

# Test it works:
echo "test" | fabric -p summarize
```

**See all available patterns:**
```bash
fabric -l
```

---

## 📁 YOUR BEST CONTENT TO PROCESS

**Sales/Coaching Calls:**
- `~/Desktop/main/LEGENDS/[LEGENDS] JON BENSON/AICA/AICA Live Call Transcripts/`
- `~/Desktop/main/LEGENDS/[LEGENDS] JON BENSON/BNSN 2.0 Transcripts/`
- `~/Desktop/main/PROOF/Testimonials/1:1 CALLS WITH CLIENTS.txt`

**Course Content:**
- `~/Downloads/RMBC2/md transcripts/` (100+ lessons)
- `~/Downloads/RMBC2/md transcripts/RMBC2_COMPLETE_COURSE.md`

**Books/Resources:**
- `~/Desktop/main/BOOKS/`
- `~/Desktop/main/LEGENDS/` (Hormozi, Kennedy, Henry)
- `~/Desktop/main/THE THIRD DOOR.md`

---

## 💰 TIME SAVINGS

**Sales calls:**
- Manual notes: 30 min
- With `sales`: 1 min
- **Saved: 29 min per call**

**Coaching follow-up:**
- Manual summary: 15 min
- With `session` + `hw`: 1 min
- **Saved: 14 min per session**

**Course material creation:**
- Manual quiz/flashcards: 4 hours
- With `quiz` + `cards`: 2 min
- **Saved: 3h 58min per course**

**10 sales calls/week = 4.8 hours saved**
**5 coaching sessions/week = 1.2 hours saved**
**Total: ~6 hours saved per week**

---

**Last Updated:** 2025-11-22
**Total Commands:** 19 (9 Tier 1 + 10 Tier 2)
**Installation:** ✅ Installed to `~/.zshrc`
**Status:** Ready to use!

---

**🎯 START HERE:**
1. Pick one call transcript
2. Run: `cat file.txt | sales`
3. See the magic happen
4. Use the rest as you need them

You've got this! 🚀
