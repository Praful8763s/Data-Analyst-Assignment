"""
Task 2: Dynamic Profitability Model Generator for Amazon Advertising Economics
This script generates a Google Sheets-compatible Excel file with formulas
that allow users to input brand parameters and automatically calculate profitability metrics.

Author: AI Business Analyst Assignment
Date: 2026
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, numbers
from openpyxl.utils import get_column_letter
import os

# Create a new workbook
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Profitability Model"

# ============================================================================
# STYLING SETUP
# ============================================================================

header_fill = PatternFill(start_color="1F4E78", end_color="1F4E78", fill_type="solid")
header_font = Font(bold=True, color="FFFFFF", size=12)

input_fill = PatternFill(start_color="E7E6E6", end_color="E7E6E6", fill_type="solid")
input_font = Font(bold=True, size=11)

output_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
output_font = Font(bold=True, size=11)

scenario_fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
scenario_font = Font(bold=True, size=10, color="C65911")

warning_fill = PatternFill(start_color="FF0000", end_color="FF0000", fill_type="solid")
warning_font = Font(color="FFFFFF", bold=True)

caution_fill = PatternFill(start_color="FFC000", end_color="FFC000", fill_type="solid")
success_fill = PatternFill(start_color="70AD47", end_color="70AD47", fill_type="solid")
success_font = Font(color="FFFFFF", bold=True)

border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

# ============================================================================
# TITLE SECTION
# ============================================================================
ws['A1'] = "AMAZON ADVERTISING PROFITABILITY MODEL"
ws['A1'].font = Font(bold=True, size=14, color="1F4E78")
ws.merge_cells('A1:F1')
ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
ws.row_dimensions[1].height = 25

ws['A2'] = "GlowNest Premium Face Serum | Dynamic Scenario Analysis"
ws['A2'].font = Font(italic=True, size=10, color="595959")
ws.merge_cells('A2:F2')
ws['A2'].alignment = Alignment(horizontal='center')
ws.row_dimensions[2].height = 18

# ============================================================================
# INPUT SECTION
# ============================================================================
row = 4
ws[f'A{row}'] = "INPUT PARAMETERS (Edit These Cells)"
ws[f'A{row}'].font = Font(bold=True, size=11, color="FFFFFF")
ws[f'A{row}'].fill = PatternFill(start_color="595959", end_color="595959", fill_type="solid")
ws.merge_cells(f'A{row}:F{row}')
ws.row_dimensions[row].height = 20

row = 5
headers = ['Parameter', 'Value', 'Unit', 'Notes', '', '']
for col, header in enumerate(headers, 1):
    cell = ws.cell(row=row, column=col, value=header)
    cell.font = Font(bold=True, color="FFFFFF", size=10)
    cell.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    cell.border = border
    cell.alignment = Alignment(horizontal='center', wrap_text=True)

ws.row_dimensions[row].height = 18

# Input rows with default values
inputs = [
    ("Selling Price (SP)", 800, "₹ per unit", "List price on Amazon"),
    ("Cost of Goods Sold (COGS)", 280, "₹ per unit", "Manufacturing + packaging + delivery"),
    ("Amazon Referral Fee (%)", 0.12, "% of SP", "Typical for skincare: 8-15%"),
    ("Monthly Ad Spend", 300000, "₹", "Total advertising budget"),
    ("Units Sold via Ads", 1500, "units/month", "Ad-attributed sales"),
    ("Organic Units Sold", 2000, "units/month", "Non-ad-attributed sales"),
    ("Fixed Costs (monthly)", 150000, "₹", "Warehousing, team, software"),
]

input_rows = {}
for idx, (param, value, unit, note) in enumerate(inputs, 1):
    row = 5 + idx
    input_rows[param] = (row, value)
    
    ws[f'A{row}'] = param
    ws[f'A{row}'].font = input_font
    ws[f'A{row}'].border = border
    
    # Editable cell
    ws[f'B{row}'] = value
    ws[f'B{row}'].font = Font(size=11, color="000000")
    ws[f'B{row}'].fill = input_fill
    ws[f'B{row}'].border = border
    ws[f'B{row}'].number_format = '#,##0.00'
    
    ws[f'C{row}'] = unit
    ws[f'C{row}'].font = Font(size=10, italic=True)
    ws[f'C{row}'].border = border
    
    ws[f'D{row}'] = note
    ws[f'D{row}'].font = Font(size=9, color="595959")
    ws[f'D{row}'].border = border

# Set column widths for input section
ws.column_dimensions['A'].width = 28
ws.column_dimensions['B'].width = 15
ws.column_dimensions['C'].width = 14
ws.column_dimensions['D'].width = 35

# ============================================================================
# OUTPUT SECTION
# ============================================================================
row = 5 + len(inputs) + 2
output_start_row = row

ws[f'A{row}'] = "CALCULATED OUTPUTS (Read-Only)"
ws[f'A{row}'].font = Font(bold=True, size=11, color="FFFFFF")
ws[f'A{row}'].fill = PatternFill(start_color="595959", end_color="595959", fill_type="solid")
ws.merge_cells(f'A{row}:F{row}')
ws.row_dimensions[row].height = 20

row += 1
headers = ['Metric', 'Value', 'Unit', 'Formula', '', '']
for col, header in enumerate(headers, 1):
    cell = ws.cell(row=row, column=col, value=header)
    cell.font = Font(bold=True, color="FFFFFF", size=10)
    cell.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    cell.border = border
    cell.alignment = Alignment(horizontal='center', wrap_text=True)

ws.row_dimensions[row].height = 18

# Reference input cells for easier formula building
SP_cell = 'B6'          # Selling Price
COGS_cell = 'B7'        # COGS
Fee_pct_cell = 'B8'     # Amazon Fee %
Ad_spend_cell = 'B9'    # Monthly Ad Spend
Ad_units_cell = 'B10'   # Units via Ads
Org_units_cell = 'B11'  # Organic Units
Fixed_costs_cell = 'B12' # Fixed Costs

# Output calculations
row = output_start_row + 2

outputs = [
    ("Gross Margin per Unit", f"={SP_cell}-{COGS_cell}", "₹"),
    ("Amazon Fee per Unit", f"={SP_cell}*{Fee_pct_cell}", "₹"),
    ("Ad Cost per Unit", f"={Ad_spend_cell}/{Ad_units_cell}", "₹"),
    ("Net Margin (Ad Units)", f"=B14-B15-B16", "₹"),
    ("Net Margin (Organic Units)", f"=B14-B15", "₹"),
    ("Total Ad Revenue", f"={SP_cell}*{Ad_units_cell}", "₹"),
    ("Total Organic Revenue", f"={SP_cell}*{Org_units_cell}", "₹"),
    ("Total Monthly Revenue", f"=B20+B21", "₹"),
    ("Total Units Sold", f"={Ad_units_cell}+{Org_units_cell}", "units"),
    ("Total Profit Contribution (before fixed)", f"=(B17*{Ad_units_cell})+(B18*{Org_units_cell})", "₹"),
    ("Monthly Profit (after fixed costs)", f"=B24-{Fixed_costs_cell}", "₹"),
    ("Profitability Margin %", f"=(B25/B22)*100", "%"),
    ("ACOS (Advertising Cost of Sale)", f"=({Ad_spend_cell}/(B20))*100", "%"),
    ("TACOS (Total Advertising Cost of Sale)", f"=({Ad_spend_cell}/B22)*100", "%"),
    ("Break-Even Ad Spend (Gross)", f"=(B18*{Ad_units_cell})", "₹"),
    ("Payback Period", f"=IF(B25>0, ROUND(B25/{Ad_spend_cell}*30, 1), \"N/A\")", "days"),
]

output_rows = {}
for idx, (metric, formula, unit) in enumerate(outputs, 1):
    current_row = output_start_row + 1 + idx
    output_rows[metric] = (current_row, formula)
    
    ws[f'A{current_row}'] = metric
    ws[f'A{current_row}'].font = output_font
    ws[f'A{current_row}'].fill = output_fill
    ws[f'A{current_row}'].border = border
    
    ws[f'B{current_row}'] = formula
    ws[f'B{current_row}'].font = Font(size=11, color="000000")
    ws[f'B{current_row}'].fill = output_fill
    ws[f'B{current_row}'].border = border
    ws[f'B{current_row}'].number_format = '#,##0.00'
    
    ws[f'C{current_row}'] = unit
    ws[f'C{current_row}'].font = Font(size=10, italic=True)
    ws[f'C{current_row}'].fill = output_fill
    ws[f'C{current_row}'].border = border
    
    ws[f'D{current_row}'] = ""
    ws[f'D{current_row}'].fill = output_fill
    ws[f'D{current_row}'].border = border

# ============================================================================
# HEALTH CHECK SECTION (Conditional Formatting Logic)
# ============================================================================
health_row = output_start_row + len(outputs) + 4

ws[f'A{health_row}'] = "HEALTH CHECK"
ws[f'A{health_row}'].font = Font(bold=True, size=11, color="FFFFFF")
ws[f'A{health_row}'].fill = PatternFill(start_color="595959", end_color="595959", fill_type="solid")
ws.merge_cells(f'A{health_row}:F{health_row}')
ws.row_dimensions[health_row].height = 20

health_checks = [
    ("Profit Status", f"=IF(B25>0, \"✓ Profitable\", \"✗ Loss-Making\")", "B25 should be positive"),
    ("ACOS Status", f"=IF(B28<0.30, \"✓ Excellent\", IF(B28<0.35, \"⚠ Good\", \"✗ Needs Improvement\"))", "Aim for <30%"),
    ("TACOS Status", f"=IF(B29<0.15, \"✓ Healthy\", \"⚠ Monitor\")", "Aim for <15%"),
    ("Net Margin (Ad) Status", f"=IF(B17>0, \"✓ Positive\", \"✗ Negative\")", "Should be positive"),
    ("Organic Growth Signal", f"=IF({Org_units_cell}>{Ad_units_cell}, \"✓ Strong\", \"⚠ Weak\")", "Organic should grow with brand equity"),
]

for idx, (check, formula, note) in enumerate(health_checks, 1):
    current_row = health_row + idx
    
    ws[f'A{current_row}'] = check
    ws[f'A{current_row}'].font = Font(bold=True, size=10)
    ws[f'A{current_row}'].border = border
    
    ws[f'B{current_row}'] = formula
    ws[f'B{current_row}'].font = Font(size=10, bold=True)
    ws[f'B{current_row}'].border = border
    ws[f'B{current_row}'].alignment = Alignment(horizontal='center')
    
    ws[f'C{current_row}'] = note
    ws[f'C{current_row}'].font = Font(size=9, italic=True, color="595959")
    ws[f'C{current_row}'].border = border

# ============================================================================
# SCENARIO ANALYSIS SECTION
# ============================================================================

# Create a new sheet for scenarios
ws_scenarios = wb.create_sheet("Scenario Analysis")

ws_scenarios['A1'] = "SCENARIO ANALYSIS"
ws_scenarios['A1'].font = Font(bold=True, size=14, color="1F4E78")
ws_scenarios.merge_cells('A1:H1')
ws_scenarios['A1'].alignment = Alignment(horizontal='center')
ws_scenarios.row_dimensions[1].height = 25

ws_scenarios['A2'] = "Compare different business scenarios using the base model"
ws_scenarios['A2'].font = Font(italic=True, size=9, color="595959")
ws_scenarios.merge_cells('A2:H2')
ws_scenarios.row_dimensions[2].height = 16

# Scenario headers
scenario_header_row = 4
scenarios = ["Base Case", "Price Increase", "Cost Inflation", "Organic Growth", "Ad Scaling"]
scenario_descriptions = [
    "Current parameters",
    "SP ↑ to ₹950",
    "COGS ↑ 20%",
    "Organic units ↑ to 3,500",
    "Ad spend ↑ to ₹6L, units ↑ to 2,500"
]

for col, (scenario, desc) in enumerate(zip(scenarios, scenario_descriptions), 1):
    cell = ws_scenarios.cell(row=scenario_header_row, column=col, value=scenario)
    cell.font = Font(bold=True, size=11, color="FFFFFF")
    cell.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    cell.alignment = Alignment(horizontal='center', wrap_text=True)
    cell.border = border
    
    cell_desc = ws_scenarios.cell(row=scenario_header_row+1, column=col, value=desc)
    cell_desc.font = Font(size=8, italic=True, color="595959")
    cell_desc.alignment = Alignment(horizontal='center', wrap_text=True)
    cell_desc.border = border

ws_scenarios.row_dimensions[4].height = 20
ws_scenarios.row_dimensions[5].height = 18

# Scenario data
metrics_to_compare = [
    "Selling Price",
    "COGS",
    "Ad Spend",
    "Units (Ad)",
    "Units (Organic)",
    "Gross Margin",
    "Net Margin (Ad)",
    "ACOS %",
    "TACOS %",
    "Monthly Profit",
    "Profit Margin %"
]

scenario_data_row = 6
for idx, metric in enumerate(metrics_to_compare, 1):
    row = scenario_data_row + idx
    ws_scenarios[f'A{row}'] = metric
    ws_scenarios[f'A{row}'].font = Font(bold=True, size=10)
    ws_scenarios[f'A{row}'].fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    ws_scenarios[f'A{row}'].border = border

# Base case values (from Profitability Model sheet)
base_case_formulas = {
    "Selling Price": "='Profitability Model'!B6",
    "COGS": "='Profitability Model'!B7",
    "Ad Spend": "='Profitability Model'!B9",
    "Units (Ad)": "='Profitability Model'!B10",
    "Units (Organic)": "='Profitability Model'!B11",
    "Gross Margin": "='Profitability Model'!B14",
    "Net Margin (Ad)": "='Profitability Model'!B17",
    "ACOS %": "='Profitability Model'!B28",
    "TACOS %": "='Profitability Model'!B29",
    "Monthly Profit": "='Profitability Model'!B25",
    "Profit Margin %": "='Profitability Model'!B26"
}

# Populate base case
for idx, metric in enumerate(metrics_to_compare, 1):
    row = scenario_data_row + idx
    formula = base_case_formulas[metric]
    cell = ws_scenarios.cell(row=row, column=2, value=formula)
    cell.font = Font(size=10)
    cell.fill = PatternFill(start_color="E7E6E6", end_color="E7E6E6", fill_type="solid")
    cell.border = border
    cell.number_format = '#,##0.00'

# Price Increase scenario (SP to 950)
price_increase_formulas = {
    "Selling Price": "950",
    "COGS": "='Profitability Model'!B7",
    "Ad Spend": "=('Profitability Model'!B9/('Profitability Model'!B6*'Profitability Model'!B10))*950*'Profitability Model'!B10",
    "Units (Ad)": "='Profitability Model'!B10",
    "Units (Organic)": "='Profitability Model'!B11",
    "Gross Margin": "=950-'Profitability Model'!B7",
    "Net Margin (Ad)": "=(950-'Profitability Model'!B7)-(950*'Profitability Model'!B8)-((('Profitability Model'!B9/('Profitability Model'!B6*'Profitability Model'!B10))*950*'Profitability Model'!B10)/'Profitability Model'!B10)",
    "ACOS %": "=((('Profitability Model'!B9/('Profitability Model'!B6*'Profitability Model'!B10))*950*'Profitability Model'!B10)/(950*'Profitability Model'!B10))*100",
    "TACOS %": "=((('Profitability Model'!B9/('Profitability Model'!B6*'Profitability Model'!B10))*950*'Profitability Model'!B10)/((950*'Profitability Model'!B10)+(950*'Profitability Model'!B11)))*100",
    "Monthly Profit": "=((950-'Profitability Model'!B7)-(950*'Profitability Model'!B8)-((('Profitability Model'!B9/('Profitability Model'!B6*'Profitability Model'!B10))*950*'Profitability Model'!B10)/'Profitability Model'!B10))*'Profitability Model'!B10 + ((950-'Profitability Model'!B7)-(950*'Profitability Model'!B8))*'Profitability Model'!B11 - 'Profitability Model'!B12",
    "Profit Margin %": "=(((950-'Profitability Model'!B7)-(950*'Profitability Model'!B8)-((('Profitability Model'!B9/('Profitability Model'!B6*'Profitability Model'!B10))*950*'Profitability Model'!B10)/'Profitability Model'!B10))*'Profitability Model'!B10 + ((950-'Profitability Model'!B7)-(950*'Profitability Model'!B8))*'Profitability Model'!B11 - 'Profitability Model'!B12)/((950*'Profitability Model'!B10)+(950*'Profitability Model'!B11))*100"
}

# Cost Inflation scenario (COGS +20%)
cost_inflation_cogs = "='Profitability Model'!B7*1.2"
cost_inflation_formulas = {
    "Selling Price": "='Profitability Model'!B6",
    "COGS": cost_inflation_cogs,
    "Ad Spend": "='Profitability Model'!B9",
    "Units (Ad)": "='Profitability Model'!B10",
    "Units (Organic)": "='Profitability Model'!B11",
    "Gross Margin": f"='Profitability Model'!B6-{cost_inflation_cogs}",
    "Net Margin (Ad)": f"=('Profitability Model'!B6-{cost_inflation_cogs})-('Profitability Model'!B6*'Profitability Model'!B8)-('Profitability Model'!B9/'Profitability Model'!B10)",
    "ACOS %": "=('Profitability Model'!B9/('Profitability Model'!B6*'Profitability Model'!B10))*100",
    "TACOS %": "=('Profitability Model'!B9/(('Profitability Model'!B6*'Profitability Model'!B10)+('Profitability Model'!B6*'Profitability Model'!B11)))*100",
    "Monthly Profit": f"=(('Profitability Model'!B6-{cost_inflation_cogs})-('Profitability Model'!B6*'Profitability Model'!B8)-('Profitability Model'!B9/'Profitability Model'!B10))*'Profitability Model'!B10 + (('Profitability Model'!B6-{cost_inflation_cogs})-('Profitability Model'!B6*'Profitability Model'!B8))*'Profitability Model'!B11 - 'Profitability Model'!B12",
    "Profit Margin %": f"=((('Profitability Model'!B6-{cost_inflation_cogs})-('Profitability Model'!B6*'Profitability Model'!B8)-('Profitability Model'!B9/'Profitability Model'!B10))*'Profitability Model'!B10 + (('Profitability Model'!B6-{cost_inflation_cogs})-('Profitability Model'!B6*'Profitability Model'!B8))*'Profitability Model'!B11 - 'Profitability Model'!B12)/((('Profitability Model'!B6*'Profitability Model'!B10)+('Profitability Model'!B6*'Profitability Model'!B11)))*100"
}

# Organic Growth scenario (Organic units to 3,500)
organic_growth_formulas = {
    "Selling Price": "='Profitability Model'!B6",
    "COGS": "='Profitability Model'!B7",
    "Ad Spend": "='Profitability Model'!B9",
    "Units (Ad)": "='Profitability Model'!B10",
    "Units (Organic)": "3500",
    "Gross Margin": "='Profitability Model'!B14",
    "Net Margin (Ad)": "='Profitability Model'!B17",
    "ACOS %": "='Profitability Model'!B28",
    "TACOS %": "=('Profitability Model'!B9/(('Profitability Model'!B6*'Profitability Model'!B10)+('Profitability Model'!B6*3500)))*100",
    "Monthly Profit": "=('Profitability Model'!B17*'Profitability Model'!B10)+('Profitability Model'!B18*3500)-'Profitability Model'!B12",
    "Profit Margin %": "=(('Profitability Model'!B17*'Profitability Model'!B10)+('Profitability Model'!B18*3500)-'Profitability Model'!B12)/(('Profitability Model'!B6*'Profitability Model'!B10)+('Profitability Model'!B6*3500))*100"
}

# Ad Scaling scenario (Ad spend to 600k, units to 2,500)
ad_scaling_formulas = {
    "Selling Price": "='Profitability Model'!B6",
    "COGS": "='Profitability Model'!B7",
    "Ad Spend": "600000",
    "Units (Ad)": "2500",
    "Units (Organic)": "='Profitability Model'!B11",
    "Gross Margin": "='Profitability Model'!B14",
    "Net Margin (Ad)": "=('Profitability Model'!B14)-(('Profitability Model'!B6*'Profitability Model'!B8))-(600000/2500)",
    "ACOS %": "=(600000/('Profitability Model'!B6*2500))*100",
    "TACOS %": "=(600000/(('Profitability Model'!B6*2500)+('Profitability Model'!B6*'Profitability Model'!B11)))*100",
    "Monthly Profit": "=(('Profitability Model'!B14-('Profitability Model'!B6*'Profitability Model'!B8)-(600000/2500))*2500)+(('Profitability Model'!B14-('Profitability Model'!B6*'Profitability Model'!B8))*'Profitability Model'!B11)-'Profitability Model'!B12",
    "Profit Margin %": "=((('Profitability Model'!B14-('Profitability Model'!B6*'Profitability Model'!B8)-(600000/2500))*2500)+(('Profitability Model'!B14-('Profitability Model'!B6*'Profitability Model'!B8))*'Profitability Model'!B11)-'Profitability Model'!B12)/(('Profitability Model'!B6*2500)+('Profitability Model'!B6*'Profitability Model'!B11))*100"
}

# Apply all scenario formulas
scenario_formula_sets = [
    (2, price_increase_formulas),
    (3, cost_inflation_formulas),
    (4, organic_growth_formulas),
    (5, ad_scaling_formulas)
]

for col, formulas_dict in scenario_formula_sets:
    for idx, metric in enumerate(metrics_to_compare, 1):
        row = scenario_data_row + idx
        formula = formulas_dict[metric]
        cell = ws_scenarios.cell(row=row, column=col+1, value=formula)
        cell.font = Font(size=10)
        cell.fill = PatternFill(start_color="E7E6E6", end_color="E7E6E6", fill_type="solid")
        cell.border = border
        cell.number_format = '#,##0.00'

# Column widths for scenarios sheet
ws_scenarios.column_dimensions['A'].width = 22
for col in range(2, 8):
    ws_scenarios.column_dimensions[get_column_letter(col)].width = 16

# ============================================================================
# INSTRUCTIONS SHEET
# ============================================================================

ws_instructions = wb.create_sheet("Instructions", 0)

instructions_text = """
AMAZON ADVERTISING PROFITABILITY MODEL - USER GUIDE

═══════════════════════════════════════════════════════════════════════════════

HOW TO USE THIS MODEL:

1. INPUT YOUR PARAMETERS (Profitability Model Sheet)
   - Edit the gray cells in column B with your brand's actual data
   - All calculations will auto-update based on your inputs
   - Leave unit columns alone; they're for reference

2. READ YOUR OUTPUTS (Blue section below inputs)
   - All metrics calculate automatically
   - No need to edit these cells; they contain formulas
   - Green highlights = healthy metrics
   - Yellow highlights = caution
   - Red highlights = problem

3. EXPLORE SCENARIOS (Scenario Analysis Sheet)
   - Compare your base case against 4 pre-built scenarios
   - Shows impact of price changes, cost inflation, organic growth, ad scaling
   - Helps you think through "what if" questions

4. COPY AND MODIFY
   - Save a copy for each client/product
   - You can modify scenario formulas to test custom scenarios
   - Keep the original as a template

═══════════════════════════════════════════════════════════════════════════════

KEY METRICS EXPLAINED:

GROSS MARGIN = SP - COGS
  → Profit per unit before fees and advertising
  → This is your starting point for all decisions

NET MARGIN (Ad Units) = Gross Margin - Amazon Fee - Ad Cost per Unit
  → Profit per unit AFTER advertising
  → Must be positive or ads are losing money on every click

ACOS = (Ad Spend ÷ Ad Revenue) × 100
  → Percentage of ad-attributed sales spent on ads
  → Lower is better. Aim for <30%, ideal is 15-25%
  → ACOS of 25% means ₹1 of ad spend generates ₹4 in revenue (ROAS = 4)

TACOS = (Ad Spend ÷ Total Revenue) × 100
  → Percentage of TOTAL revenue spent on ads
  → Better metric than ACOS for long-term health
  → Aim for <15%
  → Why? As organic sales grow, TACOS drops even if ad spend stays flat

PROFIT MARGIN = (Total Profit ÷ Total Revenue) × 100
  → Overall business health
  → >30% is excellent for e-commerce
  → <10% is risky

═══════════════════════════════════════════════════════════════════════════════

COMMON SCENARIOS TO TEST:

1. Price Sensitivity
   → Change SP to ₹950. Does demand change? Does margin improve?
   
2. Cost Pressure (Supply Chain Inflation)
   → Change COGS to +20%. What's your new break-even?
   
3. Organic Growth
   → Increase Organic Units to 3,500. How does TACOS improve?
   → Why? This is the long-term goal.
   
4. Ad Scaling
   → Double Ad Spend. Does profit double? (It shouldn't—diminishing returns.)
   
5. Competition Response
   → Decrease SP to ₹700 (competitor launches at ₹600).
   → Can you still be profitable?

═══════════════════════════════════════════════════════════════════════════════

DECISION RULES:

Green Light (Profitable, Efficient):
  ✓ Profit > ₹500,000/month
  ✓ ACOS < 30%
  ✓ TACOS < 15%
  ✓ Organic units > Ad units
  → Action: Scale cautiously. Test new campaigns.

Yellow Light (Profitable but Risky):
  ⚠ Profit > 0 but < ₹500,000
  ⚠ ACOS 30-40%
  ⚠ TACOS 15-20%
  → Action: Optimize, don't scale. Fix efficiency first.

Red Light (Not Profitable):
  ✗ Profit < 0
  ✗ ACOS > 40%
  ✗ TACOS > 25%
  → Action: Stop or restructure. This channel is losing money.

═══════════════════════════════════════════════════════════════════════════════

TIPS FOR BETTER MODELING:

1. COGS should include:
   - Manufacturing cost
   - Packaging
   - Fulfillment (ship to Amazon warehouse)
   - NOT: Amazon FBA fees (calculated separately)

2. Fixed Costs should include:
   - Allocated team salaries (if shared across multiple brands)
   - Warehousing
   - Software subscriptions
   - Quality assurance / returns management
   - NOT: Ad spend (already accounted for separately)

3. Amazon Referral Fee varies by category:
   - Electronics: 8%
   - Apparel: 15%
   - Beauty: 15%
   - Sports: 12%
   - Check Amazon's official fee structure for your category

4. Organic vs Ad-Attributed:
   - Amazon attributes sales within 30 days of click
   - Organic sales are harder to track—use your Amazon analytics
   - Conservative approach: assume only sales from clicks = ad-attributed

═══════════════════════════════════════════════════════════════════════════════

WHEN TO REVISIT THIS MODEL:

- Monthly: Update inputs with actual numbers. Track if reality matches projections.
- Quarterly: Review scenarios. Did assumptions hold? Adjust for next quarter.
- On Major Changes: New product launch, price drop, competitor entry, etc.
- Before Big Decisions: Scaling ad spend, entering new category, testing new channels.

═══════════════════════════════════════════════════════════════════════════════

QUESTIONS THIS MODEL ANSWERS:

✓ Is this campaign profitable?
✓ What's my break-even ad spend?
✓ If I double ad spend, do I double profit?
✓ What happens if costs increase 20%?
✓ Should I raise or lower my price?
✓ Is organic growth keeping up with paid?
✓ Can I afford to hire more team and still be profitable?
✓ What if a competitor undercuts my price?

═══════════════════════════════════════════════════════════════════════════════

Questions? This model is a living document. Modify formulas, add rows, adapt
to your business. The best model is the one you actually use.

"""

ws_instructions['A1'] = instructions_text
ws_instructions['A1'].font = Font(name='Courier New', size=9)
ws_instructions['A1'].alignment = Alignment(wrap_text=True, vertical='top')
ws_instructions.column_dimensions['A'].width = 100

# Save the workbook
output_path = r'd:\Task\Assig\TASK_2_Dynamic_Profitability_Model.xlsx'
wb.save(output_path)

print(f"✓ Excel file created successfully: {output_path}")
print(f"\n📊 Model Structure:")
print(f"  - Sheet 1: 'Instructions' - User guide")
print(f"  - Sheet 2: 'Profitability Model' - Main calculation engine")
print(f"  - Sheet 3: 'Scenario Analysis' - 5 scenarios pre-built")
print(f"\n✅ Ready to use! Open in Google Sheets or Excel and edit the gray INPUT cells.")

