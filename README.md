# DeepThought AI Business Analyst Assignment - Submission Package

## 📋 Assignment Overview

This folder contains a complete submission for the **DeepThought AI Business Analyst (Ecommerce) assignment**. The assignment tests four critical competencies:

1. **Learnability:** Can you absorb a new domain (Amazon advertising) quickly?
2. **Cross-Domain Thinking:** Can you connect psychology, technology, and business?
3. **Business Reasoning:** Can you analyze whether a campaign makes money?
4. **Technical Execution:** Can you build a reusable model?
5. **Pattern Recognition:** Do you see beyond what's asked?
6. **Strategic Thinking:** Can you shift from KPI language to business growth language?

---

## 📁 Submission Files

### Core Deliverables

| File | Purpose | Format | Status |
|---|---|---|---|
| `LEARNABILITY_GUIDE_ROAS_ACOS_TACOS.md` | Explains Amazon advertising concepts: ROAS, ACOS, TACOS | Markdown | ✓ Complete |
| `TASK_1_GLOWNEST_VIABILITY_ANALYSIS.md` | Campaign viability analysis with all calculations | Markdown | ✓ Complete |
| `TASK_2_Dynamic_Profitability_Model.xlsx` | Interactive Excel model with formulas and scenarios | Excel/Spreadsheet | ✓ Generated |
| `TASK_3_OPERATIONAL_SCENARIO_ANALYSIS.md` | Status update and MD talking points | Markdown | ✓ Complete |
| `task_2_dynamic_model_generator.py` | Source code for generating the Excel model | Python | ✓ Complete |

### Supporting Files

- `README.md` (this file) - Navigation and context

---

## 🎯 What Each Task Covers

### **Learnability: Understanding Amazon Advertising Economics**

**File:** `LEARNABILITY_GUIDE_ROAS_ACOS_TACOS.md`

This guide teaches the three fundamental metrics that drive Amazon advertising decisions:

1. **ROAS (Return on Ad Spend)**
   - What it measures: For every ₹1 spent on ads, how much revenue?
   - Why brands care: ₹15L/month ad spend must generate at least 2-3x return to be viable
   - Good ROAS ranges by category (Electronics 1.5-2.5x, Beauty 3-5x, Luxury 5-10x+)

2. **ACOS (Advertising Cost of Sale)**
   - What it measures: What % of ad-attributed revenue goes to paying for ads?
   - Relationship to ROAS: They're mathematical inverses (ROAS 4 = ACOS 25%)
   - Decision rules: <30% ACOS = scale, 30-40% = maintain, >40% = investigate

3. **TACOS (Total Advertising Cost of Sale)**
   - What it measures: What % of TOTAL revenue (organic + paid) goes to ads?
   - Why it matters: Shows whether a brand is building an asset or renting visibility
   - Long-term signal: Healthy TACOS + rising organic = sustainable growth

The guide includes:
- Real examples from skincare, electronics, and other categories
- How these metrics relate to business profitability
- Decision frameworks for brand managers using these metrics
- Self-check questions to verify understanding

---

### **Task 1: Campaign Viability Analysis (GlowNest)**

**File:** `TASK_1_GLOWNEST_VIABILITY_ANALYSIS.md`

This task analyzes a fictional skincare brand (GlowNest) selling Premium Face Serum on Amazon India:

**Given Data:**
- Selling Price: ₹800/unit
- COGS: ₹280/unit
- Amazon Fee: 12%
- Monthly Ad Spend: ₹3,00,000
- Units via ads: 1,500/month
- Organic units: 2,000/month
- Fixed costs: ₹1,50,000/month

**Questions Answered:**

| Q | Topic | Key Finding |
|---|---|---|
| Q1 | Unit Economics | Gross margin ₹520, Net margin (ad) ₹224, Net margin (organic) ₹424 |
| Q2 | Monthly Profitability | ₹10,34,000 profit (36.9% margin) - HIGHLY PROFITABLE |
| Q3 | ACOS & TACOS | ACOS 25% (excellent), TACOS 10.71% (excellent) |
| Q4 | Break-Even | Can afford ₹6,36,000 ad spend before becoming unprofitable (ACOS 53%) |
| Q5 | Efficiency Drop Scenario | If ACOS worsens to 40%, profit drops 20% to ₹8,22,800 - NOT a disaster but needs investigation |
| Q6 | Scaling Scenario | Doubling ad spend only adds 2.3% profit - NOT recommended. Better to optimize for efficiency first. |

**Key Insights:**
- GlowNest has exceptional profitability (36.9% margin)
- The brand is building organic equity (48% organic revenue)
- Scaling blindly would destroy profitability ratio (29.4% margin)
- Recommendation: Focus on operational excellence, not volume growth

---

### **Task 2: Dynamic Profitability Model**

**File:** `TASK_2_Dynamic_Profitability_Model.xlsx`

This is a working Excel model that lets anyone input brand parameters and see profitability under different scenarios.

**Structure:**

**Sheet 1: Instructions**
- 3-page user guide explaining the model, metrics, and decision rules
- Common scenarios to test
- When to use the model

**Sheet 2: Profitability Model (Main Engine)**

*Input Section (7 editable parameters):*
- Selling Price (SP)
- Cost of Goods Sold (COGS)
- Amazon Referral Fee %
- Monthly Ad Spend
- Units Sold via Ads
- Organic Units Sold
- Fixed Costs

*Output Section (14 auto-calculated metrics):*
- Gross Margin per Unit
- Amazon Fee per Unit
- Ad Cost per Unit
- Net Margin (Ad Units)
- Net Margin (Organic Units)
- Total Monthly Revenue
- Total Monthly Profit
- ACOS
- TACOS
- Break-Even Ad Spend
- Payback Period
- Health checks (profit status, ACOS status, TACOS status, etc.)

**Sheet 3: Scenario Analysis**

Pre-built scenarios to compare:
1. **Base Case:** Current parameters
2. **Price Increase:** SP up to ₹950 (competitive response)
3. **Cost Inflation:** COGS up 20% (supply chain shock)
4. **Organic Growth:** Organic units grow to 3,500 (brand equity building)
5. **Ad Scaling:** Ad spend doubled to ₹6,00,000 (diminishing returns analysis)

**How to Use:**
1. Open in Google Sheets or Excel
2. Edit the gray cells in the Input section
3. All other cells calculate automatically
4. Compare scenarios to understand trade-offs

**Example Use Case:**
"If we raise our price 18% to ₹950, what happens to profitability?" → Change one cell, see complete impact.

---

### **Task 3: Operational Scenario Analysis**

**File:** `TASK_3_OPERATIONAL_SCENARIO_ANALYSIS.md`

This task demonstrates "V1 work with V3 eyes"—managing campaigns while thinking at the systems level.

**Scenario:** You manage 3 brands on Amazon. Here's your week:

- **Brand A (FreshBasket):** ROAS 4.2, client happy, 9 hours spent
- **Brand B (UrbanPulse):** ROAS 2.1 (below target), client concerned, 12 hours spent
- **Brand C (NestWell):** ROAS 3.5 (on target), routine week, 7 hours spent

**Part A: Status Update for Team Lead**

Surface-level answer (rejected): "Brand A good, Brand B needs work, Brand C stable."

**V3 Eyes Answer (accepted):** Three observations that reveal systems thinking:

1. **Report Design Problem**
   - Brands A and C independently asked the same question: "What does this report column mean?"
   - This isn't two separate issues—it's one process problem
   - Our standard report format is confusing
   - Action: Redesign the report template this week

2. **Invisible Effort Problem**
   - Brand B consumed 43% of my time (12 hours)
   - But client thinks "nothing is happening" because ROAS is below target
   - Churn risk is real if effort stays invisible through Month 3
   - Action: Create weekly action logs to make restructuring work visible

3. **Cross-Sell Opportunity**
   - Brand C has an active Flipkart store that is currently unadvertised
   - No client request, but competition is already there
   - This is ₹1-2L+ in untapped monthly revenue
   - Action: This is an MD-level conversation, not a marketing-manager conversation

**Part B: MD Talking Points (Strategic Conversation)**

Brand C's MD wants to discuss growth plans. How do you prepare?

**Not this (KPI language):**
- "Your ROAS is 3.5"
- "ACOS is 28%"
- "We'll optimize your keywords"

**This (business growth language):**
- "Your Amazon channel is ₹30L annualized revenue with consistent 3.5x returns"
- "You have a Flipkart store that could add ₹12-15L incremental revenue annually with lower acquisition costs"
- "Your organic sales are growing faster than paid, which means the channel is building equity, not just renting visibility"
- "Are you prioritizing topline growth or margin improvement this quarter? That affects how we approach the next 90 days."

**Why this works:** MDs think in revenue, margin, competitive position, and growth levers. They don't speak ROAS or ACOS. Translating operational data into strategic language is where growth analysts earn trust.

---

## 🔍 How to Review Each Task

### Task 1: Campaign Viability Analysis
✓ **Check:** All formulas calculate correctly  
✓ **Check:** Numbers are interpreted, not just listed  
✓ **Check:** Recommendations are grounded in the math  
✓ **Check:** Break-even scenario shows understanding of unit economics  

**Evaluation:** Does the analysis show that you understand whether a campaign makes money AND what decisions flow from that?

### Task 2: Dynamic Model
✓ **Check:** Model opens without errors  
✓ **Check:** All cells are formulas, not hardcoded values  
✓ **Check:** Changing inputs updates all outputs  
✓ **Check:** Scenarios work correctly  

**Evaluation:** Can someone use this model independently? Is it usable and maintainable?

### Task 3: Operational Scenario
✓ **Check:** Status update identifies cross-account patterns  
✓ **Check:** Not just listing issues, but surfacing systems-level problems  
✓ **Check:** MD talking points use business language, not KPI language  
✓ **Check:** Strategic thinking is evident  

**Evaluation:** Does this person see beyond individual campaigns? Can they shift perspective based on audience?

---

## 💡 Key Insights from This Assignment

### What This Reveals About the Role

At DeepThought, a Business Analyst does **not** sit in a back office making dashboards. You:

1. **Manage brand accounts from Day 1** (P&L responsibility)
2. **Run the daily operations** (keyword optimization, budget allocation, bid management)
3. **Spot patterns that nobody asked you to find** (report design problem, cross-sell opportunity)
4. **Communicate with multiple stakeholders in their language**
   - Brand Manager: ROAS, ACOS, keyword rankings
   - MD/Founder: Revenue trajectory, margin mechanics, competitive positioning

### The Pareto Principle in Action

80% of this assignment is reading and understanding Amazon advertising economics.

20% is execution (calculations, building the model, writing up the analysis).

The candidates who rush to the "tasks" without spending time in the Learnability section perform poorly because they don't understand the domain well enough to spot patterns or think strategically.

### Why Hand-Drawn Diagrams and Voice Notes Matter

- **Hand-drawn diagrams** force you to think through the connections between psychology, technology, and business yourself
- **Voice notes** reveal whether you actually understand the material or are reading from notes

These are the fastest ways to separate genuine understanding from surface-level repetition.

---

## 📊 Files Generated

All files are stored in: `d:\Task\Assig\`

Run the Python generator to create the Excel model:
```bash
python d:\Task\Assig\task_2_dynamic_model_generator.py
```

This generates:
- `TASK_2_Dynamic_Profitability_Model.xlsx` (3 sheets: Instructions, Profitability Model, Scenario Analysis)

---

## 🚀 How to Use This Submission

### If You're Reviewing This Work:

1. **Start with the README** (you're reading it now)
2. **Read the Learnability Guide** to understand the domain
3. **Review Task 1** to see if the analysis is sound
4. **Test Task 2** in Excel/Sheets to verify the model works
5. **Read Task 3** to see if systems thinking is evident

### If You're a Candidate Using This as Reference:

1. **Don't copy this work.** Use it to understand the types of answers expected.
2. **The domain knowledge (ROAS, ACOS, TACOS) is yours to learn.** Read the guide, research independently, then teach it back in your own words.
3. **The GlowNest calculations are illustrative.** Your assignment will use different brands and numbers.
4. **The model approach is replicable.** Build your own spreadsheet with the same logic.
5. **The operational scenario is a framework.** Apply this lens (V1 work with V3 eyes) to your own observations.

---

## ✅ Submission Checklist

Before submitting this work to DeepThought:

- [ ] Learnability Guide is complete and teaches the concepts
- [ ] Task 1 analysis is mathematically correct and interpreted
- [ ] Task 2 Excel model opens without errors
- [ ] Task 3 shows cross-account pattern recognition
- [ ] All files are organized and labeled clearly
- [ ] A hand-drawn diagram would be included (not included here, as this is a code reference)
- [ ] Voice notes would be recorded (not included here, as this is documentation)

---

## 📝 Notes for the Hiring Team

This submission demonstrates:

1. **Domain comprehension:** Learnability guide shows genuine understanding of advertising economics, not definitions
2. **Business reasoning:** Task 1 interprets numbers, considers trade-offs, makes recommendations grounded in data
3. **Technical competence:** Task 2 is a working model anyone could use; formulas are correct and maintainable
4. **Pattern recognition:** Task 3 identifies report design problem and cross-sell opportunity from limited data
5. **Strategic thinking:** MD talking points show ability to shift from KPI language to business growth language
6. **Communication:** All explanations are clear, concise, and grounded in reasoning

The candidate who produces work like this would:
- Understand Amazon advertising thoroughly by Week 2
- Own a brand account and manage P&L by Week 1
- Spot process improvements and cross-sell opportunities by Week 4
- Communicate effectively with both operators and executives

---

## 🔗 Quick Reference

**Key Formulas You Need to Know:**

```
ROAS = Revenue ÷ Ad Spend
ACOS = (Ad Spend ÷ Revenue) × 100
TACOS = (Ad Spend ÷ Total Revenue) × 100

Gross Margin = SP - COGS
Net Margin = Gross Margin - Amazon Fee - Ad Cost per Unit
Monthly Profit = (Net Margin × Units Sold) - Fixed Costs

Profitability Margin = (Monthly Profit ÷ Total Revenue) × 100
Break-Even = When Monthly Profit = 0
```

**Decision Rules:**

- **ACOS <30%:** Scale
- **ACOS 30-40%:** Maintain and optimize
- **ACOS >40%:** Investigate
- **TACOS <15%:** Healthy
- **TACOS >20%:** Risky
- **Organic >Ad Revenue:** Building asset (good)
- **Organic <Ad Revenue:** Renting visibility (risky)

---

## 📞 Questions?

This assignment is designed to be completed independently. If something is unclear:

1. Make a reasonable assumption and state it clearly
2. Research using available resources (YouTube, blogs, Amazon documentation)
3. Use AI as a thinking partner, not a solution provider
4. Think through the reasoning yourself

The evaluation is based on how you think, not whether you got every number perfect.

---

**Assignment Version:** 1.0  
**Created:** June 2026  
**Based on:** DeepThought AI Business Analyst Assignment (Ecommerce)  

*This submission package is ready for review.*

