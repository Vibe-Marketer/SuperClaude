# === FABRIC AI SHORTCUTS (Tiers 1 + 2) ===
# Added by Claude Code on 2025-11-22
# Usage: cat file.txt | sales
# Or: sales < file.txt
# Or with drag & drop: sales (then drag file into terminal)

# TIER 1: Daily Use (Must Have)
alias sales='fabric -p analyze_sales_call'              # Sales techniques, objections, what worked
alias session='fabric -p create_summary'                # Full session summary for clients
alias wisdom='fabric -p extract_wisdom'                 # Key takeaways from any content
alias hw='fabric -p extract_recommendations'            # Action items and homework
alias sum3='fabric -p summarize'                        # 2-3 paragraph summary
alias quiz='fabric -p create_quiz'                      # 10-15 quiz questions
alias upsell='fabric -p extract_business_ideas'         # Upsell opportunities, product ideas
alias real='fabric -p extract_primary_problem'          # The REAL core problem
alias deep='fabric -p extract_insights'                 # Deep patterns and strategic insights

# TIER 2: Weekly Use (Very Useful)
alias better='fabric -p improve_writing'                # Better writing instantly
alias FAQs='fabric -p extract_questions'                # Build FAQs
alias chapters='fabric -p create_video_chapters'        # Chapter titles + timestamps
alias lines5='fabric -p create_5_sentence_summary'      # Perfect for CRM notes
alias hooks='fabric -p create_better_frame'             # 10-20 attention-grabbing hooks
alias cards='fabric -p create_flash_cards'              # Study flashcards
alias claims='fabric -p analyze_claims'                 # Fact-check claims
alias fail='fabric -p analyze_mistakes'                 # Learn from failures
alias objections='fabric -p analyze_sales_call'         # Extract objections (same as sales)
alias tone='fabric -p analyze_personality'              # Voice/tone/brand analysis

# TIER 3: Monthly Use (Situational Power)
alias compare='fabric -p compare_and_contrast'          # Side-by-side comparison
alias debate='fabric -p analyze_debate'                 # Argument analysis
alias present='fabric -p analyze_presentation'          # Presentation breakdown
alias feedback='fabric -p analyze_product_feedback'     # Customer feedback patterns
alias ideas='fabric -p extract_ideas'                   # All ideas mentioned
alias essay='fabric -p write_essay'                     # Generate essay
alias easycode='fabric -p explain_code'                 # Code documentation
alias books='fabric -p extract_book_ideas'              # Book concepts/frameworks
alias yt='fabric -p youtube_summary'                    # YouTube video summary
alias interview='fabric -p answer_interview_question'   # Interview answers

# TIER 3 (Content Creation)
alias mozi='fabric -p create_hormozi_offer'             # Hormozi value equation offer
alias one-liner='fabric -p create_aphorisms'            # Wisdom quotes/one-liners
alias news='fabric -p create_newsletter_entry'          # Newsletter content
alias blog='fabric -p enrich_blog_post'                 # Enhanced blog post
alias keynote='fabric -p create_keynote'                # Keynote presentation
alias story='fabric -p create_story_explanation'        # Explain via storytelling
alias email='fabric -p create_formal_email'             # Professional email
alias reading='fabric -p create_reading_plan'           # Reading plan
alias tweet='fabric -p tweet'                           # Twitter threads
alias mini-essay='fabric -p write_micro_essay'          # Short-form essay

# TIER 4: Specialized Use Cases
alias risks='fabric -p analyze_risk'                    # Risk analysis
alias props='fabric -p analyze_proposition'             # Business proposition analysis
alias prose='fabric -p analyze_prose'                   # Literary analysis
alias false='fabric -p find_logical_fallacies'          # Logical fallacy detection
alias hidden='fabric -p find_hidden_message'            # Find subtext
alias predict='fabric -p extract_predictions'           # Extract predictions
alias solution='fabric -p extract_primary_solution'     # Main solution discussed
alias features='fabric -p extract_product_features'     # Product features
alias partners='fabric -p extract_sponsors'             # Sponsors/partners/affiliates
alias sources='fabric -p extract_references'            # Citations/sources

# TIER 4 (Development & Tech)
alias bettercode='fabric -p coding_master'              # Advanced coding help
alias addcode='fabric -p create_coding_feature'         # Generate code feature
alias newcode='fabric -p create_coding_project'         # Full project architecture
alias reviewcode='fabric -p review_code'                # Code review
alias designdoc='fabric -p create_design_document'      # Technical design doc
alias prd='fabric -p create_prd'                        # Product Requirements Doc
alias git='fabric -p create_git_diff_commit'            # Generate commit messages
alias pr='fabric -p write_pull-request'                 # Pull request description

# TIER 5: Nice to Have
alias article='fabric -p extract_article_wisdom'        # Article wisdom
alias jokes='fabric -p extract_jokes'                   # Extract humor
alias characters='fabric -p extract_characters'         # Character profiles
alias recipe='fabric -p extract_recipe'                 # Recipe extraction
alias sing='fabric -p extract_song_meaning'             # Song lyrics meaning
alias zoom='fabric -p summarize_meeting'                # Meeting summary
alias paper='fabric -p analyze_paper'                   # Academic paper analysis
alias lecture='fabric -p summarize_lecture'             # Lecture summary
alias prompt='fabric -p improve_prompt'                 # Better AI prompts
alias trans='fabric -p translate'                       # Language translation

# === ADD YOUR OWN FABRIC SHORTCUTS ===
# Usage: add shortcut-name pattern-name "Description"
# Example: add mypattern extract_wisdom "My custom wisdom extractor"
add() {
    if [ $# -lt 2 ]; then
        echo "Usage: add [shortcut-name] [fabric-pattern] [optional-description]"
        echo ""
        echo "Example: add mypattern extract_wisdom \"My custom wisdom extractor\""
        echo ""
        echo "Available patterns: fabric -l"
        return 1
    fi

    local shortcut=$1
    local pattern=$2
    local description=${3:-"Custom pattern"}

    # Add to ~/.zshrc
    echo "" >> ~/.zshrc
    echo "# Custom added: $(date)" >> ~/.zshrc
    echo "alias $shortcut='fabric -p $pattern'  # $description" >> ~/.zshrc

    # Reload
    source ~/.zshrc

    echo "✅ Added shortcut: $shortcut → fabric -p $pattern"
    echo "📝 Description: $description"
    echo "🔄 Reloaded! You can now use: $shortcut"
}

