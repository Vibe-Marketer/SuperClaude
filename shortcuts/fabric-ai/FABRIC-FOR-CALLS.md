# 🎯 FABRIC FOR COACHING/SALES/TEACHING CALLS

The patterns that will actually make you money.

---

## 💰 SALES CALL ANALYSIS (The Money Makers)

### **`analyze_sales_call`** ⭐⭐⭐⭐⭐
**THE BIG ONE** - Analyzes sales calls for techniques, objections, outcomes.

```bash
cat sales-transcript.txt | fabric -p analyze_sales_call
```

**What you get:**
- Sales techniques used
- Objections raised and how handled
- Decision points
- What worked / didn't work
- Improvement suggestions

**Use for:** Every single sales call transcript

---

### **`extract_business_ideas`**
Pull business opportunities mentioned in calls.

```bash
cat coaching-call.txt | fabric -p extract_business_ideas
```

**Use for:** Finding upsell opportunities, product ideas from customer pain points

---

### **`extract_primary_problem`**
What's the REAL problem the person has?

```bash
cat call-transcript.txt | fabric -p extract_primary_problem
```

**Use for:** Understanding what clients actually need vs what they say they need

---

### **`extract_primary_solution`**
What solution was offered/discussed?

```bash
cat call-transcript.txt | fabric -p extract_primary_solution
```

**Use for:** Tracking what solutions you're proposing, seeing patterns

---

## 🎓 COACHING/TEACHING ANALYSIS

### **`extract_questions`**
Pull all questions asked during the call.

```bash
cat coaching-call.txt | fabric -p extract_questions
```

**Gold for:**
- Creating FAQ docs
- Identifying common student questions
- Building training materials

---

### **`extract_recommendations`**
What advice/recommendations were given?

```bash
cat coaching-call.txt | fabric -p extract_recommendations
```

**Use for:**
- Creating action item lists
- Follow-up emails
- Building playbooks from successful calls

---

### **`create_summary`** ⭐⭐⭐⭐⭐
Detailed summary of the entire call.

```bash
cat long-call.txt | fabric -p create_summary
```

**Use for:**
- Quick call reviews
- Sending to clients: "Here's what we discussed"
- Team handoffs

---

### **`create_5_sentence_summary`**
Ultra-short version.

```bash
cat call-transcript.txt | fabric -p create_5_sentence_summary
```

**Use for:**
- CRM notes
- Quick reference
- Email subject lines

---

### **`extract_insights`** ⭐⭐⭐⭐⭐
Deep insights and patterns from content.

```bash
cat transcript.txt | fabric -p extract_insights
```

**Use for:**
- Finding trends across multiple calls
- Identifying what's working
- Strategic planning

---

### **`analyze_mistakes`**
What went wrong and why?

```bash
cat bad-call.txt | fabric -p analyze_mistakes
```

**Use for:**
- Learning from failed sales calls
- Improving coaching techniques
- Training new team members

---

## 📚 LONG CONTENT PROCESSING (Books/Courses/Videos)

### **`extract_wisdom`** ⭐⭐⭐⭐⭐
Pull actionable wisdom and key insights.

```bash
cat course-transcript.txt | fabric -p extract_wisdom
```

**Returns:**
- Key ideas
- Actionable advice
- Quotes worth remembering
- Practical applications

**Use for:**
- Course transcripts
- Book summaries
- Long teaching sessions

---

### **`extract_book_ideas`**
Specifically for books - pulls main concepts.

```bash
cat book-transcript.txt | fabric -p extract_book_ideas
```

---

### **`extract_article_wisdom`**
Like extract_wisdom but optimized for articles/written content.

```bash
cat article.txt | fabric -p extract_article_wisdom
```

---

### **`create_video_chapters`**
Break long videos into chapters with timestamps.

```bash
cat video-transcript.txt | fabric -p create_video_chapters
```

**Use for:**
- Course videos
- Webinar recordings
- Long training sessions

---

### **`create_quiz`**
Generate quiz questions from content.

```bash
cat course-lesson.txt | fabric -p create_quiz
```

**Gold for:**
- Testing student knowledge
- Creating engagement
- Building course materials

---

### **`create_flash_cards`**
Generate study flashcards.

```bash
cat training-content.txt | fabric -p create_flash_cards
```

---

### **`summarize_lecture`**
Designed specifically for educational content.

```bash
cat lecture-transcript.txt | fabric -p summarize_lecture
```

---

## 🎬 VIDEO/TRANSCRIPT SPECIFIC

### **`extract_sponsors`**
Find all sponsors/partners mentioned.

```bash
cat transcript.txt | fabric -p extract_sponsors
```

**Use for:** Finding partnership opportunities, tracking referrals

---

### **`extract_product_features`**
Pull product/service features discussed.

```bash
cat product-demo-call.txt | fabric -p extract_product_features
```

**Use for:** Building product docs, understanding what clients care about

---

### **`extract_controversial_ideas`**
Find spicy/controversial points.

```bash
cat call-transcript.txt | fabric -p extract_controversial_ideas
```

**Use for:** Finding objections before they become problems

---

## 🔥 POWER WORKFLOWS FOR YOUR USE CASES

### Sales Call Analysis (After Every Call):
```bash
# 1. Get the overview
cat call.txt | fabric -p analyze_sales_call > analysis.txt

# 2. Extract the core problem
cat call.txt | fabric -p extract_primary_problem >> analysis.txt

# 3. Pull business opportunities
cat call.txt | fabric -p extract_business_ideas >> analysis.txt

# 4. Get 5-sentence summary for CRM
cat call.txt | fabric -p create_5_sentence_summary > crm-note.txt
```

---

### Coaching Call Follow-Up:
```bash
# 1. Create summary for client
cat call.txt | fabric -p create_summary > summary.txt

# 2. Extract recommendations (action items)
cat call.txt | fabric -p extract_recommendations > action-items.txt

# 3. Pull insights for your records
cat call.txt | fabric -p extract_insights > insights.txt

# Email them: summary + action items
```

---

### Course/Book Processing:
```bash
# 1. Extract wisdom (main takeaways)
cat course.txt | fabric -p extract_wisdom > key-points.txt

# 2. Create chapters/outline
cat course.txt | fabric -p create_video_chapters > chapters.txt

# 3. Generate quiz for students
cat course.txt | fabric -p create_quiz > quiz.txt

# 4. Make flashcards
cat course.txt | fabric -p create_flash_cards > flashcards.txt
```

---

### Multi-Call Pattern Analysis (GOLD):
```bash
# Run on 10+ sales calls, then analyze the combined insights
cat call1.txt call2.txt call3.txt | fabric -p extract_insights > patterns.txt

# See what questions come up repeatedly
cat call1.txt call2.txt call3.txt | fabric -p extract_questions > faq.txt

# Find common objections
cat call*.txt | fabric -p extract_primary_problem > common-problems.txt
```

---

## 🎯 YOUR TOP 5 MUST-USE PATTERNS

Based on coaching/sales/teaching:

1. **`analyze_sales_call`** - After every sales call
2. **`extract_wisdom`** - For courses/books/long content
3. **`extract_insights`** - Find patterns across multiple calls
4. **`extract_recommendations`** - Create action items
5. **`create_summary`** - Send to clients after calls

---

## 💡 REAL EXAMPLES

### Example 1: Post-Sales Call
```bash
cat "Sales Call - John Doe - 2025-01-22.txt" | fabric -p analyze_sales_call
```

**Output might include:**
- "Client expressed budget concerns around $5k"
- "Strong interest in automation features"
- "Mentioned competitor XYZ"
- "Suggested follow-up: Send case study"

---

### Example 2: Coaching Session
```bash
cat "Coaching - Sarah - Week 3.txt" | fabric -p extract_recommendations
```

**Output:**
- "Focus on morning routine for 30 days"
- "Track metrics daily in spreadsheet"
- "Read chapter 5 before next session"

---

### Example 3: Course Material
```bash
cat "Module 1 - Introduction to Marketing.txt" | fabric -p create_quiz
```

**Output:**
- "Q1: What are the 4 Ps of marketing?"
- "Q2: Define market segmentation"
- etc.

---

## 🚀 SHORTCUTS TO ADD

Want me to create these shortcuts?

```bash
# Sales
sales-analyze call.txt        # Full sales analysis
sales-problems call.txt        # Extract problems
sales-summary call.txt         # 5-sentence summary

# Coaching
coach-summary call.txt         # Full summary
coach-actions call.txt         # Action items
coach-insights call.txt        # Deep insights

# Content
content-wisdom course.txt      # Extract wisdom
content-quiz lesson.txt        # Generate quiz
content-chapters video.txt     # Create chapters
```

Let me know if you want these!

---

## 📊 BATCH PROCESSING (Process Multiple Calls at Once)

```bash
# Analyze all sales calls from January
for file in sales-calls-jan/*.txt; do
  echo "Processing $file..."
  cat "$file" | fabric -p analyze_sales_call > "analysis-$(basename $file)"
done

# Extract common questions from all coaching calls
cat coaching-calls/*.txt | fabric -p extract_questions > all-questions.txt
```

---

## 💰 ROI EXAMPLES

**Sales calls:**
- 1 hour call → 30 min manual notes
- With Fabric: 1 min automated analysis
- **Savings: 29 min per call**
- 10 calls/week = **4.8 hours saved**

**Course creation:**
- 2-hour course → 4 hours to create materials
- With Fabric: 5 min to generate quiz, flashcards, chapters
- **Savings: 3+ hours per course**

**Client follow-ups:**
- Manual summary: 15 min per call
- Fabric summary: 30 seconds
- **Savings: 14.5 min per call**

---

**TL;DR - Start Here:**
```bash
# After a sales call:
cat transcript.txt | fabric -p analyze_sales_call

# After a coaching call:
cat transcript.txt | fabric -p create_summary
cat transcript.txt | fabric -p extract_recommendations

# For long courses/books:
cat content.txt | fabric -p extract_wisdom
cat content.txt | fabric -p create_quiz
```

These 5 commands will handle 90% of your use cases.

---

**Last Updated:** 2025-11-22
**Your killer apps:** Sales analysis, coaching follow-ups, course material generation
