# Execution Guide: How to Use the DeepThought Assignment Submission

## 📍 Current Location
All files are stored in: **`d:\Task\Assig\`**

## ✅ What Has Been Completed

### 1. **Learnability Phase** ✓
**File:** `LEARNABILITY_GUIDE_ROAS_ACOS_TACOS.md`

A comprehensive guide explaining the three core Amazon advertising concepts:

- **ROAS (Return on Ad Spend):** For every ₹1 spent, how much revenue comes back?
- **ACOS (Advertising Cost of Sale):** What % of revenue goes to paying for ads?
- **TACOS (Total Advertising Cost of Sale):** What % of TOTAL revenue goes to ads?

**Content includes:**
- Definition and calculation for each metric
- Real-world examples (₹15L/month ad spend scenarios)
- Why brands care about each metric
- Category-specific benchmarks (Electronics, Beauty, Luxury, etc.)
- How metrics relate to each other (ROAS and ACOS are inverses)
- When to tolerate high ACOS vs. when it's a problem
- Why organic sales growth matters more than ad efficiency alone
- Self-check questions to verify understanding

**How to use for voice note preparation:**
1. Read this guide thoroughly (2-3 times)
2. Understand not just the definitions but the business logic
3. Practice explaining to a colleague without reading notes
4. Record a 5+ minute voice note teaching these concepts naturally
5. Include examples the guide doesn't mention (your own creation)

---

### 2. **Task 1: Campaign Viability Analysis** ✓
**File:** `TASK_1_GLOWNEST_VIOWNEST_VIABILITY_ANALYSIS.md`

Complete analysis of a fictional skincare brand (GlowNest) selling Premium Face Serum on Amazon India.

**Includes all 6 questions answered:**

| Q | Topic | Answer |
|---|---|---|
| Q1 | Unit Economics | Gross margin ₹520, Ad net margin ₹224, Organic net margin ₹424 |
| Q2 | Monthly Profitability | ₹10,34,000 (36.9% profitability margin) |
| Q3 | ACOS & TACOS Analysis | ACOS 25% (excellent), TACOS 10.71% (excellent), 48% organic revenue |
| Q4 | Break-Even Analysis | Can afford ₹6,36,000 ad spend (ACOS 53%) before unprofitable |
| Q5 | Efficiency Drop Scenario | If ACOS worsens to 40%, profit drops ₹2,11,200 (-20.4%) |
| Q6 | Scaling Scenario | Doubling ad spend only adds ₹24,000 profit (2.3%) - NOT recommended |

**Each answer includes:**
- Mathematical calculations shown step-by-step
- Interpretation of what the numbers mean
- Business implications and recommendations
- Context for decision-making

**How to use for your submission:**
1. Review the calculations to verify methodology
2. Understand the reasoning behind each recommendation
3. Adapt this analysis structure for your own brand data
4. Prepare 2-3 minute voice note explaining:
   - What surprised you about the numbers?
   - What would you tell the brand?
   - How would this affect your strategy?

---

### 3. **Task 2: Dynamic Profitability Model** ✓
**File:** `TASK_2_Dynamic_Profitability_Model.xlsx`

A working Excel spreadsheet with three sheets:

#### **Sheet 1: Instructions** (User Guide)
- 3-page explanation of how to use the model
- Key metrics defined
- Common scenarios to test
- Decision rules for different profitability levels
- When to revisit and update the model

#### **Sheet 2: Profitability Model** (Main Engine)
**Input Section (7 editable cells):**
- Selling Price (SP)
- Cost of Goods Sold (COGS)
- Amazon Referral Fee %
- Monthly Ad Spend
- Units Sold via Ads
- Organic Units Sold
- Fixed Costs (monthly)

**Output Section (14 auto-calculated metrics):**
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
- Health checks (Profit Status, ACOS Status, TACOS Status)

All calculations use formulas, not hardcoded values. Change any input and all outputs update automatically.

#### **Sheet 3: Scenario Analysis**
Pre-built comparisons of 5 scenarios:
1. Base Case (current parameters)
2. Price Increase (SP ↑ to ₹950)
3. Cost Inflation (COGS ↑ 20%)
4. Organic Growth (Organic units ↑ to 3,500)
5. Ad Scaling (Ad spend ↑ to ₹6,00,000, units ↑ to 2,500)

**How to use:**
1. Open in Google Sheets or Microsoft Excel
2. Edit ONLY the gray cells in the Input section
3. All blue cells calculate automatically
4. Compare scenarios to understand trade-offs
5. Test "what if" questions relevant to your brand

**Example Use Cases:**
- "If we raise our price 18% to ₹950, what happens to profitability?"
- "Can we survive a 20% increase in COGS?"
- "If organic grows to 3,500 units, what happens to TACOS?"
- "Is it profitable to double our ad spend?"

---

### 4. **Task 3: Operational Scenario Analysis** ✓
**File:** `TASK_3_OPERATIONAL_SCENARIO_ANALYSIS.md`

Demonstration of "V1 work with V3 eyes"—managing daily operations while thinking at the systems level.

#### **Part A: Status Update for Team Lead**
Shows how to write a status update that reveals pattern recognition:

**Three key observations:**

1. **Report Design Problem**
   - Two clients independently asked the same question
   - This is a process problem, not two separate issues
   - Recommendation: Redesign report template

2. **Invisible Effort Problem (Churn Risk)**
   - Brand B consumed 43% of time but client feels nothing is happening
   - Deep keyword restructuring is invisible
   - If effort stays invisible through Month 3, client will churn
   - Recommendation: Create weekly action logs to show work progress

3. **Cross-Sell Opportunity**
   - Brand C has unadvertised Flipkart store
   - This is ₹1-2L+ untapped monthly revenue
   - Competitors already advertising there
   - Recommendation: This is an MD-level conversation

#### **Part B: Strategic Conversation with MD**
Shows how to prepare talking points for executive-level discussion:

**Key translations (KPI language → business language):**
- "ROAS 3.5" → "₹30L annualized revenue with consistent returns"
- "ACOS 28%" → "Cost per acquisition is optimized"
- "Optimize keywords" → "Here's a growth lever: test Flipkart channel"

**Why this matters:**
- MDs don't care about ROAS or ACOS
- MDs care about revenue, margin, competitive positioning, growth
- Same data, different lens, different conversation

**How to use:**
1. Review the status update format
2. Practice identifying patterns across multiple data points
3. Learn to write in business language for executive audiences
4. Prepare thinking shift analysis for your voice note:
   - How did your thinking change from "operational" to "strategic"?
   - What information would you need that you don't have?
   - How do you decide when to talk to Brand Manager vs. MD?

---

### 5. **Python Code for Model Generation** ✓
**File:** `task_2_dynamic_model_generator.py`

Source code that generated the Excel model. Use this if you want to:
- Understand how the model was built
- Modify the structure for your own needs
- Generate new models with different parameters
- Add additional sheets or metrics

**How to run:**
```bash
python d:\Task\Assig\task_2_dynamic_model_generator.py
```

This regenerates the Excel file with all formulas and formatting.

---

### 6. **README and Documentation** ✓
**File:** `README.md` and `EXECUTION_GUIDE.md` (this file)

Complete documentation of the submission including:
- What each file contains
- How to evaluate each task
- Key insights and decision rules
- Quick reference formulas
- How to use this work as a study guide

---

## 🎯 How to Complete Your Own Submission

### Phase 1: Learning (Days 1-2, 80% effort)

1. **Read the Learnability Guide thoroughly**
   - Understand ROAS, ACOS, TACOS
   - Why they matter for a brand spending ₹15L/month on ads
   - How they relate to each other
   - Why organic growth is the long-term strategy

2. **Research independently**
   - Watch YouTube videos on Amazon advertising
   - Read blog posts on e-commerce profitability
   - Understand your specific product category (if assigned)
   - Build genuine understanding, not memorized definitions

3. **Draw your hand-drawn diagram**
   - Sketch on paper how Psychology → Technology → Business
   - Show connections between all three domains
   - Label arrows showing data flow and influence
   - Make sure it reflects YOUR thinking, not a template

4. **Record your learnability voice note**
   - 5+ minutes explaining ROAS, ACOS, TACOS
   - Talk naturally, don't read from notes
   - Give an example that wasn't in your source material
   - Show you understand connections, not just definitions

### Phase 2: Execution (Days 2-3, 20% effort)

1. **Task 1: Campaign Viability Analysis**
   - Follow the same structure as GlowNest analysis
   - Your assignment will have different brand data
   - Calculate all metrics step-by-step
   - Interpret results and make recommendations
   - Record 2-3 minute voice note on your approach

2. **Task 2: Dynamic Profitability Model**
   - Build in Google Sheets or Excel
   - Create similar structure: Inputs → Calculations → Outputs
   - Use formulas, not hardcoded values
   - Test scenarios to verify model works
   - Include instructions for other users

3. **Task 3: Operational Scenario**
   - Write status update identifying cross-account patterns
   - Prepare MD talking points in business language
   - Record 2-3 minute voice note on thinking shift
   - Explain what patterns you noticed and why they matter

### Phase 3: Refinement (Day 3)

1. **Review your own work**
2. **Check all calculations**
3. **Test model scenarios**
4. **Rewrite voice notes if needed**
5. **Ensure all files are clear and labeled**
6. **Create single Google Drive folder with all files**
7. **Set sharing permissions to "anyone with link can view"**

---

## 🔍 Quality Checklist

Before submitting, verify:

### Learnability
- [ ] Can teach ROAS in 1 minute without notes
- [ ] Can explain why ACOS and ROAS are inverses
- [ ] Can give an example of TACOS that wasn't in source material
- [ ] Hand-drawn diagram shows connections, not just boxes
- [ ] 5+ minute voice note is fluent (not reading from paper)

### Task 1: Viability
- [ ] All 6 questions answered with calculations
- [ ] Numbers are mathematically correct
- [ ] Interpretations go beyond just stating the number
- [ ] Recommendations are grounded in data
- [ ] 2-3 minute voice note explains approach naturally

### Task 2: Model
- [ ] Opens without errors in Excel/Sheets
- [ ] All calculations use formulas, not values
- [ ] Changing inputs updates all outputs
- [ ] Scenarios work correctly
- [ ] User can understand how to use it
- [ ] Model is maintainable and replicable

### Task 3: Operations
- [ ] Status update identifies patterns across accounts
- [ ] Not just listing KPIs but surfacing systems problems
- [ ] MD talking points use business language (revenue, margin, growth)
- [ ] No ROAS or ACOS when talking to MD
- [ ] 2-3 minute voice note shows thinking shift

---

## 📊 Example: How to Think About Each Task

### Task 1 in Your Head:

"Brand X is spending ₹3L/month on ads. Are they making money?
- Calculate: costs, margins, net profit
- Interpret: Is the profit enough to scale? To hire more team?
- Recommend: If they double ad spend, do they double profit? (No, usually not)
- Advise: What should they focus on instead?"

### Task 2 in Your Head:

"Build something someone else can use without asking me questions.
- Clear inputs (gray cells they can edit)
- Automatic calculations (blue cells with formulas)
- Examples/scenarios (showing 'what if' possibilities)
- Instructions (so they don't get lost)"

### Task 3 in Your Head:

"What did I notice that nobody asked me to look for?
- Pattern 1: Multiple clients asking same question (process problem)
- Pattern 2: High effort, invisible to client (churn risk)
- Pattern 3: Unused asset, untapped opportunity (growth lever)
- Then: How do I communicate this to different audiences?"

---

## 💡 Pro Tips

1. **On the voice notes:**
   - Record multiple times, use the best take
   - Speak naturally, as if talking to a colleague
   - Include pauses and thinking ("so that means...")
   - Show your reasoning, not just conclusions

2. **On the calculations:**
   - Show your work, even if step-by-step seems obvious
   - This proves you understand, not just luck
   - Examiners want to follow your logic

3. **On the diagrams:**
   - Messy is fine, wrong connections are not
   - Show data flow between domains
   - Label everything
   - Take a photo/scan at good resolution

4. **On strategic thinking:**
   - Don't guess at MD priorities
   - Use data to infer (organic 48%→ MD cares about building assets)
   - Ask questions to confirm ("Are you prioritizing topline or margin?")
   - Never present ROAS to an MD

5. **On time management:**
   - 80% reading/understanding takes 2 full days
   - Don't rush this phase
   - 20% execution takes 1 day
   - One day for refinement/review

---

## 🚀 After Submission

If you get selected for the interview:

1. **Be ready to explain your reasoning** for each decision
2. **Know your numbers** (you should know them cold)
3. **Be able to defend trade-offs** ("Why not scale? Because...")
4. **Ask strategic questions** ("If margins are 30%, what's your growth target?")
5. **Show pattern recognition** ("I noticed X across Y situations...")

The interview will likely ask:
- "Walk me through your Task 1 analysis"
- "Show me your model and explain one scenario"
- "Tell me about a pattern you noticed"
- "How would you explain TACOS to an MD who only knows revenue?"

---

## 📝 Final Notes

This submission package demonstrates:

✓ **Domain mastery** (you understand Amazon advertising)  
✓ **Technical execution** (you can build working models)  
✓ **Business reasoning** (you can interpret data and recommend action)  
✓ **Systems thinking** (you see patterns others miss)  
✓ **Communication** (you can speak multiple languages: KPI, business, strategic)  

All of this is what DeepThought evaluates. The assignment isn't about "right" answers; it's about how you think, learn, and see connections.

---

**Last Updated:** June 4, 2026  
**Status:** Ready for use  
**Next Step:** Follow Phase 1 learning, prepare your own submission

Good luck! 🎯

