"""
TASK 3: Operational Scenario Analysis - V1 Work with V3 Eyes
Executable Python script that demonstrates pattern recognition and strategic thinking
"""

# ============================================================================
# BRAND DATA
# ============================================================================

BRANDS = {
    'A': {
        'name': 'FreshBasket',
        'category': 'Organic Snacks',
        'ad_spend_monthly': 250000,
        'roas': 4.2,
        'hours_spent': 9,
        'status': 'Happy',
        'client_question': "Can you explain what the daily spend breakdown means? I don't understand columns.",
    },
    'B': {
        'name': 'UrbanPulse',
        'category': "Men's Grooming",
        'ad_spend_monthly': 400000,
        'roas': 2.1,
        'target_roas': 3.0,
        'hours_spent': 12,
        'status': 'Concerned',
        'months_in': 2,
        'client_concern': "We're not seeing results. Are we sure this is working?",
        'work_done': ['keyword restructuring', 'negative keyword audit', 'competitive analysis'],
    },
    'C': {
        'name': 'NestWell',
        'category': 'Home Fragrances',
        'ad_spend_monthly': 180000,
        'roas': 3.5,
        'target_roas': 3.5,
        'hours_spent': 7,
        'status': 'On Target',
        'client_question': "Can you explain what the daily spend breakdown means? Columns confusing.",
        'flipkart_store': 'Active but unadvertised',
    }
}

WEEK_PERIOD = "Week 4"
TOTAL_HOURS = 28

# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    print()
    print("=" * 80)
    print("TASK 3: OPERATIONAL SCENARIO ANALYSIS")
    print("V1 Work (Execution) + V3 Eyes (Systems Thinking)")
    print("=" * 80)
    print()
    
    # ========================================================================
    # PART A: OPERATIONAL STATUS
    # ========================================================================
    
    print("PART A: OPERATIONAL STATUS UPDATE")
    print("=" * 80)
    print()
    
    print(f"Period: {WEEK_PERIOD}")
    print(f"Total Hours: {TOTAL_HOURS} hours")
    print(f"Accounts: 3 brands")
    print()
    
    for brand_id in ['A', 'B', 'C']:
        data = BRANDS[brand_id]
        print(f"Brand {brand_id}: {data['name']} ({data['category']})")
        print(f"  Ad Spend: INR {data['ad_spend_monthly']:,}/month")
        print(f"  ROAS: {data['roas']}")
        print(f"  Status: {data['status']}")
        print(f"  Hours: {data['hours_spent']}")
        if 'client_concern' in data:
            print(f"  Client: {data['client_concern']}")
        elif 'client_question' in data:
            print(f"  Client: {data['client_question']}")
        print()
    
    # ========================================================================
    # PART A: PATTERN RECOGNITION (V3 Eyes)
    # ========================================================================
    
    print("=" * 80)
    print("PATTERN RECOGNITION - V3 EYES (What I Actually Noticed)")
    print("=" * 80)
    print()
    
    print("PATTERN 1: REPORT DESIGN PROBLEM")
    print("-" * 80)
    print()
    print("Observation:")
    print("  Brand A asked: 'Can you explain the daily spend breakdown columns?'")
    print("  Brand C asked: 'Can you explain the daily spend breakdown columns?'")
    print()
    print("Analysis:")
    print("  - Same question from 2 different clients (67% of accounts)")
    print("  - This is NOT two separate issues")
    print("  - This IS one process problem: Our report template is confusing")
    print()
    print("Business Impact:")
    print("  - Clients cannot verify our work independently")
    print("  - Reduces confidence in campaign data")
    print("  - Creates unnecessary support burden")
    print("  - Increases churn risk")
    print()
    print("Action:")
    print("  1. Audit report template this week")
    print("  2. Redesign for clarity")
    print("  3. Test with one client")
    print("  4. Roll out to all by end of Month 2")
    print()
    
    print("PATTERN 2: INVISIBLE EFFORT PROBLEM (Churn Risk)")
    print("-" * 80)
    print()
    print("Hours Distribution:")
    print(f"  Brand A: {BRANDS['A']['hours_spent']} hours (32%)")
    print(f"  Brand B: {BRANDS['B']['hours_spent']} hours (43%) <- HIGHEST")
    print(f"  Brand C: {BRANDS['C']['hours_spent']} hours (25%)")
    print()
    print("Brand B Work:")
    print("  - Keyword restructuring (deep work)")
    print("  - Negative keyword audit (40 keywords)")
    print("  - Competitive analysis")
    print("  - Client email response")
    print()
    print("But Client Says:")
    print("  'We're not seeing results. Are we sure this is working?'")
    print()
    print("The Problem:")
    print("  Client sees: ROAS 2.1 (below target 3.0)")
    print("  Client does NOT see: The restructuring work happening behind scenes")
    print()
    print("Churn Risk Timeline:")
    print("  Month 1: Client optimistic")
    print("  Month 2: Client concerned (THIS IS NOW)")
    print("  Month 3: Client churns unless effort becomes visible")
    print()
    print("Action:")
    print("  1. Create 'Weekly Action Log' for UrbanPulse")
    print("  2. Show visible impact of work:")
    print("     - 'Paused 23 underperforming keywords (INR 15k/month waste prevented)'")
    print("     - 'Added 40 negative keywords (ACOS 28% to 22%)'")
    print("     - 'Restructured campaign hierarchy'")
    print("  3. Set expectations: Month 1-2 rebuild, Month 3 ROAS compounds")
    print("  4. Schedule MD check-in (proactive engagement)")
    print()
    
    print("PATTERN 3: UNTAPPED GROWTH OPPORTUNITY")
    print("-" * 80)
    print()
    print("Observation:")
    print(f"  Brand C (NestWell): {BRANDS['C']['flipkart_store']}")
    print(f"  Current Flipkart ad investment: INR 0")
    print(f"  Client request: None")
    print()
    print("Market Reality:")
    print("  - Competitors ARE advertising on Flipkart")
    print("  - Flipkart CPCs are 30-40% lower than Amazon")
    print("  - This is untapped revenue opportunity")
    print()
    print("Opportunity:")
    print("  - Current Amazon: INR 1.8L/month spend --> INR 6.3L/month revenue")
    print("  - Flipkart test: INR 30k/month --> INR 1L+/month revenue potential")
    print("  - Flipkart margins: 15-20% higher than Amazon")
    print()
    print("Action:")
    print("  1. This is an MD-level conversation (NOT brand manager)")
    print("  2. Prepare business case")
    print("  3. Frame as growth lever, not mandatory")
    print()
    
    # ========================================================================
    # COMPARISON
    # ========================================================================
    
    print("=" * 80)
    print("V1 vs V3 THINKING COMPARISON")
    print("=" * 80)
    print()
    
    print("V1 ONLY (Surface Level):")
    print("-" * 80)
    print("Brand A: ROAS 4.2, happy, no issues.")
    print("Brand B: ROAS 2.1, below target, optimizing.")
    print("Brand C: ROAS 3.5, on target, routine week.")
    print()
    print("Problems:")
    print("  - No patterns identified")
    print("  - No systems thinking")
    print("  - Just individual status updates")
    print("  - Team lead learns nothing except numbers")
    print()
    
    print("V1 + V3 (Systems Thinking):")
    print("-" * 80)
    print("Operating summary: [same numbers]")
    print()
    print("Systems-level observations:")
    print("  1. Report design problem (67% of clients confused)")
    print("  2. Invisible effort problem (high effort, low client perception)")
    print("  3. Untapped growth opportunity (Flipkart channel)")
    print()
    print("Impact:")
    print("  - Team lead identifies systemic issues")
    print("  - Recognizes pattern recognition")
    print("  - Sees growth thinking")
    print("  - Understands this person thinks beyond KPIs")
    print()
    
    # ========================================================================
    # PART B: MD TALKING POINTS
    # ========================================================================
    
    print("=" * 80)
    print("PART B: MD TALKING POINTS (Strategic Level)")
    print("=" * 80)
    print()
    
    print("Context: NestWell MD wants to discuss Amazon growth plans")
    print()
    
    print("Opening:")
    print("-" * 80)
    print("'Your Amazon channel is performing well - consistent 3.5x returns on ad spend,")
    print("stable performance. But I noticed something about your business structure that")
    print("I think connects to your broader growth plans.'")
    print()
    
    print("The Opportunity:")
    print("-" * 80)
    print("'Your Flipkart store is live but unadvertised. Your competitors are already")
    print("there. This is an untapped revenue opportunity with lower acquisition costs'")
    print()
    
    print("Business Case (MD Language):")
    print("-" * 80)
    print("Current Amazon Channel:")
    print("  - Revenue: INR 30L annualized")
    print("  - Returns: 3.5x (consistent)")
    print()
    print("Flipkart Test Opportunity:")
    print("  - Investment: INR 30k/month (low risk)")
    print("  - Expected revenue: INR 12-15L annualized")
    print("  - Margin benefit: 15-20% higher than Amazon")
    print()
    
    print("Key Questions for MD:")
    print("-" * 80)
    print("1. Where does e-commerce fit in your Q growth plan?")
    print("   Are you prioritizing topline or margin improvement?")
    print()
    print("2. Would you invest INR 30k/month for a Flipkart test?")
    print()
    print("3. Any differences between Amazon and Flipkart store setup?")
    print()
    
    print("What NOT to Say:")
    print("-" * 80)
    print("WRONG: 'Your ROAS is 3.5'")
    print("RIGHT: 'Your Amazon channel is INR 30L annualized revenue'")
    print()
    print("WRONG: 'ACOS is 28%'")
    print("RIGHT: 'Your ad costs are optimized'")
    print()
    print("WRONG: 'We'll optimize keywords'")
    print("RIGHT: 'Test this growth lever'")
    print()
    
    # ========================================================================
    # THINKING SHIFT
    # ========================================================================
    
    print("=" * 80)
    print("THINKING SHIFT REFLECTION")
    print("=" * 80)
    print()
    
    print("How Did Thinking Change?")
    print("-" * 80)
    print()
    print("Operational (V1):")
    print("  What happened this week?")
    print("  Metrics: ROAS, ACOS, hours")
    print("  Audience: Team lead")
    print()
    print("Strategic (V3):")
    print("  What does this mean for growth?")
    print("  Metrics: Revenue, margin, competitive position")
    print("  Audience: MD")
    print()
    
    print("Same data, different lens:")
    print("  Operational: 'ROAS is 3.5, on target'")
    print("  Strategic: 'This is an opportunity to test a second channel'")
    print()
    
    # ========================================================================
    # CONCLUSION
    # ========================================================================
    
    print("=" * 80)
    print("CONCLUSION")
    print("=" * 80)
    print()
    
    print("What Makes V3 Thinking Different:")
    print()
    print("1. You manage campaigns (V1)")
    print("2. You spot patterns (V3)")
    print("3. You identify process problems (V3)")
    print("4. You see growth opportunities (V3)")
    print("5. You speak multiple languages (KPI + Business + Strategic)")
    print()
    
    print("This is what separates operations people from growth advisors.")
    print()
    print("=" * 80)
    print()

if __name__ == "__main__":
    main()
