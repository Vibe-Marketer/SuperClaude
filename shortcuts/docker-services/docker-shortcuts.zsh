

# === START/STOP ALL SERVICES ===
alias start='echo "🚀 Starting all services..." && archon-start && mindbase-start && echo "✅ All services started!"'
alias stop='echo "🛑 Stopping all services..." && archon-stop && mindbase-stop && echo "✅ All services stopped!"'
alias services='docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"'


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
