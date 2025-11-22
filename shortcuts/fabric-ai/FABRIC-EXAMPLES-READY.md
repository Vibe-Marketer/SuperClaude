# 🎯 READY-TO-RUN FABRIC EXAMPLES

Copy/paste these into a **NEW terminal window** to try them out!

---

## ⚡ QUICK START

### 1. Start Your Services (Do This First!)
```bash
start
```
This starts both Archon and Mindbase in the background.

---

## 🔥 REAL EXAMPLES WITH YOUR FILES

### Example 1: Analyze a Sales Call (AICA)
```bash
cd ~/Desktop/main/LEGENDS/\[LEGENDS\]\ JON\ BENSON/AICA/AICA\ Live\ Call\ Transcripts/AICA\ LIVE\ Individual\ Calls

# Full sales analysis
sales < "9. AICA-Week8-Live-Call.txt"

# Get the real problem
real < "9. AICA-Week8-Live-Call.txt"

# Find upsell opportunities
upsell < "9. AICA-Week8-Live-Call.txt"

# 5-sentence summary for CRM
lines5 < "9. AICA-Week8-Live-Call.txt"
```

---

### Example 2: Process RMBC2 Course (Create Teaching Materials)
```bash
cd ~/Downloads/RMBC2/md\ transcripts

# Extract key wisdom
wisdom < "01-Intro_01_Welcome_To_RMBC2_Course_Overview.md"

# Generate quiz questions for students
quiz < "01-Intro_01_Welcome_To_RMBC2_Course_Overview.md"

# Create flashcards
cards < "01-Intro_01_Welcome_To_RMBC2_Course_Overview.md"

# Create video chapters
chapters < "01-Intro_01_Welcome_To_RMBC2_Course_Overview.md"
```

---

### Example 3: Process VSL Theory Module
```bash
cd ~/Downloads/RMBC2/md\ transcripts

# Extract wisdom from VSL module
wisdom < "04-VSL-Theory_02_VSL_Fundamentals_Classic_Structure.md"

# Create quiz
quiz < "04-VSL-Theory_02_VSL_Fundamentals_Classic_Structure.md"

# Get hooks for marketing
hooks < "04-VSL-Theory_02_VSL_Fundamentals_Classic_Structure.md"
```

---

### Example 4: Analyze "The Third Door" Book
```bash
cd ~/Desktop/main

# Extract wisdom
wisdom < "THE THIRD DOOR.md"

# Quick summary
sum3 < "THE THIRD DOOR.md"

# Create one-liners for social media
one-liner < "THE THIRD DOOR.md"

# Get hooks
hooks < "THE THIRD DOOR.md"
```

---

### Example 5: Process Client Testimonial Calls
```bash
cd ~/Desktop/main/PROOF/Testimonials

# Create session summary to send to client
session < "1:1 CALLS WITH CLIENTS.txt"

# Extract action items
hw < "1:1 CALLS WITH CLIENTS.txt"

# Find patterns across calls
deep < "1:1 CALLS WITH CLIENTS.txt"
```

---

### Example 6: Analyze BNSN 2.0 Call
```bash
cd ~/Desktop/main/LEGENDS/\[LEGENDS\]\ JON\ BENSON/BNSN\ 2.0\ Transcripts

# Sales analysis
sales < "BNSN 2.0 | Jon <> Andrew - Updates & New Wizard Project - June 02.txt"

# Extract business ideas
upsell < "BNSN 2.0 | Jon <> Andrew - Updates & New Wizard Project - June 02.txt"

# Find the real problem
real < "BNSN 2.0 | Jon <> Andrew - Updates & New Wizard Project - June 02.txt"
```

---

### Example 7: Create Hormozi-Style Offer from Your Content
```bash
cd ~/Desktop/main/LEGENDS

# Find a Hormozi content file first
ls -la | grep -i hormozi

# Then create an offer from it
# mozi < [HORMOZI-FILE].md
```

---

### Example 8: Batch Process ALL RMBC2 Modules
```bash
cd ~/Downloads/RMBC2/md\ transcripts

# Extract wisdom from ALL modules
for file in *.md; do
  echo "=== Processing: $file ===" >> RMBC2-ALL-WISDOM.txt
  wisdom < "$file" >> RMBC2-ALL-WISDOM.txt
  echo "" >> RMBC2-ALL-WISDOM.txt
done

# Now open the file
open RMBC2-ALL-WISDOM.txt
```

---

### Example 9: Process Complete RMBC2 Course (The Big One!)
```bash
cd ~/Downloads/RMBC2/md\ transcripts

# Extract wisdom from entire course
wisdom < "RMBC2_COMPLETE_COURSE.md" > RMBC2-Complete-Wisdom.txt

# Create comprehensive quiz
quiz < "RMBC2_COMPLETE_COURSE.md" > RMBC2-Complete-Quiz.txt

# Get all hooks from entire course
hooks < "RMBC2_COMPLETE_COURSE.md" > RMBC2-All-Hooks.txt

# Open results
open RMBC2-Complete-Wisdom.txt
```

---

### Example 10: Full Sales Call Analysis Pipeline
```bash
cd ~/Desktop/main/LEGENDS/\[LEGENDS\]\ JON\ BENSON/AICA/AICA\ Live\ Call\ Transcripts/AICA\ LIVE\ Individual\ Calls

FILE="9. AICA-Week8-Live-Call.txt"

# Create full analysis package
echo "🔥 FULL SALES CALL ANALYSIS" > analysis.txt
echo "================================" >> analysis.txt
echo "" >> analysis.txt

echo "📊 SALES ANALYSIS:" >> analysis.txt
sales < "$FILE" >> analysis.txt
echo "" >> analysis.txt

echo "🎯 REAL PROBLEM:" >> analysis.txt
real < "$FILE" >> analysis.txt
echo "" >> analysis.txt

echo "💰 UPSELL OPPORTUNITIES:" >> analysis.txt
upsell < "$FILE" >> analysis.txt
echo "" >> analysis.txt

echo "🚫 OBJECTIONS:" >> analysis.txt
objections < "$FILE" >> analysis.txt
echo "" >> analysis.txt

echo "📝 CRM SUMMARY:" > crm-note.txt
lines5 < "$FILE" >> crm-note.txt

# Open results
open analysis.txt
open crm-note.txt
```

---

## 💡 DRAG & DROP METHOD (Easiest!)

1. Open Terminal
2. Type: `sales` (or any command)
3. **Drag a file from Finder into Terminal**
4. Press Enter

Done! 🎉

---

## 🎨 TEST IT FIRST (No Files Needed)

```bash
# Test with simple text:
echo "The client mentioned they're struggling with their marketing funnel and have budget constraints. They want to improve conversions but aren't sure where to start. They're currently spending $5k/month on ads with minimal ROI." | sales

# Test summary:
echo "This is a long story about how I learned direct response marketing from Dan Kennedy. It took many years of studying his materials, implementing his strategies, testing and refining. Eventually I got really good at creating high-converting VSLs and now I teach it to others through my RMBC2 course. The key is understanding the psychology of persuasion and crafting compelling offers." | sum3

# Test improve writing:
echo "i think that marketing is good and stuff and you should do it because it helps" | better
```

---

## 🔄 YOUR DAILY WORKFLOW

### Morning (Start Services):
```bash
start
```

### After a Sales Call:
```bash
cd [call-transcript-folder]
sales < call.txt > analysis.txt
real < call.txt >> analysis.txt
upsell < call.txt >> analysis.txt
lines5 < call.txt > crm.txt
```

### After Coaching Session:
```bash
session < call.txt > email-to-client.txt
hw < call.txt >> email-to-client.txt
```

### Processing Course Content:
```bash
wisdom < lesson.txt > key-points.txt
quiz < lesson.txt > student-quiz.txt
```

### End of Day (Services keep running!):
```bash
# No need to stop - they run in background
# Or if you want to stop them:
stop
```

---

## 📂 YOUR FILE LOCATIONS (Quick Reference)

```bash
# Sales/Coaching Calls
~/Desktop/main/LEGENDS/[LEGENDS] JON BENSON/AICA/AICA Live Call Transcripts/
~/Desktop/main/LEGENDS/[LEGENDS] JON BENSON/BNSN 2.0 Transcripts/
~/Desktop/main/PROOF/Testimonials/

# RMBC2 Course
~/Downloads/RMBC2/md transcripts/

# Books
~/Desktop/main/BOOKS/
~/Desktop/main/THE THIRD DOOR.md

# Legends Content
~/Desktop/main/LEGENDS/
```

---

## 🆘 IF SOMETHING DOESN'T WORK

**"Command not found":**
```bash
# Reload your shell:
source ~/.zshrc

# Or just open a NEW terminal window
```

**Check Fabric is working:**
```bash
which fabric
fabric -l
```

---

## 🎯 START HERE (Right Now!)

1. **Open a NEW terminal window**
2. **Run this test:**
```bash
echo "Test: The client needs help with their marketing strategy and has budget concerns." | sales
```
3. **If that works, try a real file:**
```bash
cd ~/Downloads/RMBC2/md\ transcripts
wisdom < "01-Intro_01_Welcome_To_RMBC2_Course_Overview.md"
```

---

**💪 You're ready! Pick an example and go!**

**Last Updated:** 2025-11-22
