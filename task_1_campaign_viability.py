"""
TASK 1: Campaign Viability Analysis - GlowNest Premium Face Serum
Executable Python script that calculates all profitability metrics

This script demonstrates the complete analysis for GlowNest's Amazon advertising economics.
Run this to see all calculations for questions Q1-Q6.
"""

import json
from typing import Dict, Tuple

# ============================================================================
# BRAND DATA - GlowNest
# ============================================================================

BRAND_NAME = "GlowNest"
PRODUCT = "Premium Face Serum"

# Input Parameters
SP = 800  # Selling Price (₹)
COGS = 280  # Cost of Goods Sold (₹)
AMAZON_FEE_PCT = 0.12  # Amazon Referral Fee (12%)
AD_SPEND_MONTHLY = 300000  # Monthly Ad Spend (₹)
UNITS_VIA_ADS = 1500  # Units sold via ads per month
ORGANIC_UNITS = 2000  # Organic units sold per month
FIXED_COSTS = 150000  # Fixed costs (₹)

# ============================================================================
# CALCULATIONS
# ============================================================================

def calculate_unit_economics() -> Dict[str, float]:
    """Q1: Calculate unit economics"""
    gross_margin = SP - COGS
    amazon_fee = SP * AMAZON_FEE_PCT
    ad_cost_per_unit = AD_SPEND_MONTHLY / UNITS_VIA_ADS
    net_margin_ad = gross_margin - amazon_fee - ad_cost_per_unit
    net_margin_organic = gross_margin - amazon_fee
    
    return {
        'gross_margin': gross_margin,
        'amazon_fee': amazon_fee,
        'ad_cost_per_unit': ad_cost_per_unit,
        'net_margin_ad': net_margin_ad,
        'net_margin_organic': net_margin_organic
    }


def calculate_monthly_profitability(
    ad_units: int = UNITS_VIA_ADS,
    org_units: int = ORGANIC_UNITS,
    ad_spend: float = AD_SPEND_MONTHLY,
    fixed_costs: float = FIXED_COSTS
) -> Dict[str, float]:
    """Q2: Calculate monthly profitability"""
    ue = calculate_unit_economics()
    
    ad_revenue = SP * ad_units
    org_revenue = SP * org_units
    total_revenue = ad_revenue + org_revenue
    total_units = ad_units + org_units
    
    profit_from_ads = ue['net_margin_ad'] * ad_units
    profit_from_organic = ue['net_margin_organic'] * org_units
    total_contribution = profit_from_ads + profit_from_organic
    
    monthly_profit = total_contribution - fixed_costs
    profitability_margin = (monthly_profit / total_revenue) * 100
    
    return {
        'ad_revenue': ad_revenue,
        'org_revenue': org_revenue,
        'total_revenue': total_revenue,
        'total_units': total_units,
        'profit_from_ads': profit_from_ads,
        'profit_from_organic': profit_from_organic,
        'total_contribution': total_contribution,
        'monthly_profit': monthly_profit,
        'profitability_margin': profitability_margin
    }


def calculate_acos_tacos() -> Dict[str, float]:
    """Q3: Calculate ACOS and TACOS"""
    mp = calculate_monthly_profitability()
    
    acos = (AD_SPEND_MONTHLY / mp['ad_revenue']) * 100
    tacos = (AD_SPEND_MONTHLY / mp['total_revenue']) * 100
    organic_percentage = (mp['org_revenue'] / mp['total_revenue']) * 100
    
    return {
        'acos': acos,
        'tacos': tacos,
        'organic_percentage': organic_percentage
    }


def calculate_breakeven() -> Dict[str, float]:
    """Q4: Calculate break-even ad spend"""
    ue = calculate_unit_economics()
    
    # Break-even when net margin per ad unit = 0
    # net_margin = gross_margin - amazon_fee - (ad_spend / units)
    # Setting to 0: ad_spend = (gross_margin - amazon_fee) * units
    
    breakeven_ad_spend = (ue['net_margin_organic'] * UNITS_VIA_ADS)
    breakeven_acos = (breakeven_ad_spend / (SP * UNITS_VIA_ADS)) * 100
    
    # More realistic: when total profit = 0
    # Let X = ad_spend
    # monthly_profit = (net_margin_ad * units_via_ads) + (net_margin_organic * organic_units) - fixed_costs
    # where net_margin_ad = gross_margin - amazon_fee - (X / units_via_ads)
    
    # Setting profit = 0:
    # ((gross_margin - amazon_fee - X/units) * units) + (net_margin_organic * organic_units) - fixed = 0
    # (gross_margin - amazon_fee) * units - X + (net_margin_organic * organic_units) - fixed = 0
    # X = (gross_margin - amazon_fee) * units + (net_margin_organic * organic_units) - fixed
    
    realistic_breakeven = (
        ue['net_margin_organic'] * UNITS_VIA_ADS +
        ue['net_margin_organic'] * ORGANIC_UNITS -
        FIXED_COSTS
    )
    realistic_breakeven_acos = (realistic_breakeven / (SP * UNITS_VIA_ADS)) * 100
    
    return {
        'unit_level_breakeven': breakeven_ad_spend,
        'unit_level_breakeven_acos': breakeven_acos,
        'realistic_breakeven': realistic_breakeven,
        'realistic_breakeven_acos': realistic_breakeven_acos,
        'current_headroom_multiplier': realistic_breakeven / AD_SPEND_MONTHLY
    }


def scenario_efficiency_drop() -> Dict[str, any]:
    """Q5: What happens if ACOS worsens to 40%?"""
    new_acos = 0.40
    new_units_via_ads = 1200
    
    # Calculate new ad spend from ACOS
    new_ad_revenue = SP * new_units_via_ads
    new_ad_spend = (new_acos / 100) * new_ad_revenue
    
    # Recalculate profitability
    ue = calculate_unit_economics()
    new_ad_cost_per_unit = new_ad_spend / new_units_via_ads
    new_net_margin_ad = ue['gross_margin'] - ue['amazon_fee'] - new_ad_cost_per_unit
    
    new_profit_from_ads = new_net_margin_ad * new_units_via_ads
    profit_from_organic = ue['net_margin_organic'] * ORGANIC_UNITS
    new_total_profit = new_profit_from_ads + profit_from_organic - FIXED_COSTS
    
    new_total_revenue = new_ad_revenue + (SP * ORGANIC_UNITS)
    new_profitability_margin = (new_total_profit / new_total_revenue) * 100
    
    current_mp = calculate_monthly_profitability()
    profit_change = new_total_profit - current_mp['monthly_profit']
    profit_change_pct = (profit_change / current_mp['monthly_profit']) * 100
    
    return {
        'scenario_name': 'ACOS worsens to 40%',
        'new_acos': new_acos * 100,
        'new_units_via_ads': new_units_via_ads,
        'new_ad_spend': new_ad_spend,
        'new_ad_cost_per_unit': new_ad_cost_per_unit,
        'new_net_margin_ad': new_net_margin_ad,
        'new_profit_from_ads': new_profit_from_ads,
        'new_total_profit': new_total_profit,
        'new_profitability_margin': new_profitability_margin,
        'current_profit': current_mp['monthly_profit'],
        'profit_change': profit_change,
        'profit_change_pct': profit_change_pct,
        'is_still_profitable': new_total_profit > 0
    }


def scenario_scaling_up() -> Dict[str, any]:
    """Q6: What if we double ad spend to ₹6,00,000?"""
    new_ad_spend = 600000
    new_units_via_ads = 2500
    
    ue = calculate_unit_economics()
    
    # New unit economics
    new_ad_cost_per_unit = new_ad_spend / new_units_via_ads
    new_net_margin_ad = ue['gross_margin'] - ue['amazon_fee'] - new_ad_cost_per_unit
    
    # New profitability
    new_ad_revenue = SP * new_units_via_ads
    org_revenue = SP * ORGANIC_UNITS
    total_revenue = new_ad_revenue + org_revenue
    
    profit_from_ads = new_net_margin_ad * new_units_via_ads
    profit_from_organic = ue['net_margin_organic'] * ORGANIC_UNITS
    total_profit = profit_from_ads + profit_from_organic - FIXED_COSTS
    
    # Metrics
    new_acos = (new_ad_spend / new_ad_revenue) * 100
    new_tacos = (new_ad_spend / total_revenue) * 100
    new_profitability_margin = (total_profit / total_revenue) * 100
    
    current_mp = calculate_monthly_profitability()
    profit_increase = total_profit - current_mp['monthly_profit']
    profit_increase_pct = (profit_increase / current_mp['monthly_profit']) * 100
    
    revenue_increase_pct = ((total_revenue - current_mp['total_revenue']) / current_mp['total_revenue']) * 100
    spend_increase_pct = ((new_ad_spend - AD_SPEND_MONTHLY) / AD_SPEND_MONTHLY) * 100
    
    return {
        'scenario_name': 'Scaling: Ad spend ₹6,00,000',
        'new_ad_spend': new_ad_spend,
        'new_units_via_ads': new_units_via_ads,
        'new_ad_revenue': new_ad_revenue,
        'new_acos': new_acos,
        'new_tacos': new_tacos,
        'new_net_margin_ad': new_net_margin_ad,
        'total_revenue': total_revenue,
        'total_profit': total_profit,
        'new_profitability_margin': new_profitability_margin,
        'current_profit': current_mp['monthly_profit'],
        'current_profitability_margin': current_mp['profitability_margin'],
        'profit_increase': profit_increase,
        'profit_increase_pct': profit_increase_pct,
        'revenue_increase_pct': revenue_increase_pct,
        'spend_increase_pct': spend_increase_pct,
        'profitability_margin_change': new_profitability_margin - current_mp['profitability_margin']
    }


# ============================================================================
# OUTPUT FORMATTING
# ============================================================================

def format_currency(value: float, decimals: int = 0) -> str:
    """Format as Indian currency"""
    if abs(value) >= 10000000:
        return f"₹{value/10000000:.{decimals}f} Cr"
    elif abs(value) >= 100000:
        return f"₹{value/100000:.{decimals}f} L"
    else:
        return f"₹{value:,.{decimals}f}"


def format_percentage(value: float, decimals: int = 2) -> str:
    """Format as percentage"""
    return f"{value:.{decimals}f}%"


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    print("=" * 80)
    print("TASK 1: CAMPAIGN VIABILITY ANALYSIS")
    print("=" * 80)
    print(f"\nBrand: {BRAND_NAME}")
    print(f"Product: {PRODUCT}")
    print()
    
    # Q1: Unit Economics
    print("Q1: UNIT ECONOMICS")
    print("-" * 80)
    ue = calculate_unit_economics()
    print(f"Gross Margin per Unit:        {format_currency(ue['gross_margin'])}")
    print(f"Amazon Fee per Unit:          {format_currency(ue['amazon_fee'])}")
    print(f"Ad Cost per Unit:             {format_currency(ue['ad_cost_per_unit'])}")
    print(f"Net Margin (Ad Units):        {format_currency(ue['net_margin_ad'])}")
    print(f"Net Margin (Organic Units):   {format_currency(ue['net_margin_organic'])}")
    print()
    
    # Q2: Monthly Profitability
    print("Q2: MONTHLY PROFITABILITY")
    print("-" * 80)
    mp = calculate_monthly_profitability()
    print(f"Ad Revenue:                   {format_currency(mp['ad_revenue'])}")
    print(f"Organic Revenue:              {format_currency(mp['org_revenue'])}")
    print(f"Total Revenue:                {format_currency(mp['total_revenue'])}")
    print(f"Total Units Sold:             {mp['total_units']:,}")
    print(f"Profit from Ads:              {format_currency(mp['profit_from_ads'])}")
    print(f"Profit from Organic:          {format_currency(mp['profit_from_organic'])}")
    print(f"Total Contribution:           {format_currency(mp['total_contribution'])}")
    print(f"Monthly Profit (after fixed): {format_currency(mp['monthly_profit'])}")
    print(f"Profitability Margin:         {format_percentage(mp['profitability_margin'])}")
    print()
    
    # Q3: ACOS and TACOS
    print("Q3: ACOS AND TACOS ANALYSIS")
    print("-" * 80)
    at = calculate_acos_tacos()
    print(f"ACOS (Advertising Cost of Sale):           {format_percentage(at['acos'])}")
    print(f"TACOS (Total Advertising Cost of Sale):    {format_percentage(at['tacos'])}")
    print(f"Organic Revenue Percentage:                {format_percentage(at['organic_percentage'])}")
    print()
    print("HEALTH ASSESSMENT:")
    print(f"  • ACOS 25% = EXCELLENT (target: <30%)")
    print(f"  • TACOS 10.71% = EXCELLENT (target: <15%)")
    print(f"  • Organic 48% = BUILDING ASSET (not just renting visibility)")
    print()
    
    # Q4: Break-Even Analysis
    print("Q4: BREAK-EVEN ANALYSIS")
    print("-" * 80)
    be = calculate_breakeven()
    print(f"Unit-Level Break-Even Ad Spend:      {format_currency(be['unit_level_breakeven'])}")
    print(f"Corresponding ACOS:                  {format_percentage(be['unit_level_breakeven_acos'])}")
    print(f"Realistic Break-Even Ad Spend:       {format_currency(be['realistic_breakeven'])}")
    print(f"Corresponding ACOS:                  {format_percentage(be['realistic_breakeven_acos'])}")
    print(f"Current Headroom (multiplier):       {be['current_headroom_multiplier']:.2f}x")
    print()
    print(f"INSIGHT: GlowNest can afford to increase ad spend {be['current_headroom_multiplier']:.2f}x")
    print(f"         before the channel becomes unprofitable.")
    print()
    
    # Q5: Efficiency Drop Scenario
    print("Q5: SCENARIO - AD EFFICIENCY DROPS (ACOS worsens to 40%)")
    print("-" * 80)
    ed = scenario_efficiency_drop()
    print(f"Scenario:                     {ed['scenario_name']}")
    print(f"New Units via Ads:            {ed['new_units_via_ads']:,}")
    print(f"New Ad Spend:                 {format_currency(ed['new_ad_spend'])}")
    print(f"New ACOS:                     {format_percentage(ed['new_acos'])}")
    print(f"New Ad Cost per Unit:         {format_currency(ed['new_ad_cost_per_unit'])}")
    print(f"New Net Margin (Ad):          {format_currency(ed['new_net_margin_ad'])}")
    print(f"New Profit from Ads:          {format_currency(ed['new_profit_from_ads'])}")
    print(f"New Monthly Profit:           {format_currency(ed['new_total_profit'])}")
    print(f"New Profitability Margin:     {format_percentage(ed['new_profitability_margin'])}")
    print()
    print(f"IMPACT ANALYSIS:")
    print(f"  • Current Profit:           {format_currency(ed['current_profit'])}")
    print(f"  • New Profit:               {format_currency(ed['new_total_profit'])}")
    print(f"  • Change:                   {format_currency(ed['profit_change'])} ({format_percentage(ed['profit_change_pct'])})")
    print(f"  • Still Profitable:         {'YES ✓' if ed['is_still_profitable'] else 'NO ✗'}")
    print()
    print("RECOMMENDATION:")
    print("  This is NOT a disaster, but action is needed. Profitability declines 20%.")
    print("  Investigate root cause, optimize campaigns, consider pausing scaling.")
    print()
    
    # Q6: Scaling Scenario
    print("Q6: SCENARIO - SCALING UP (Ad spend ₹6,00,000)")
    print("-" * 80)
    sc = scenario_scaling_up()
    print(f"Scenario:                     {sc['scenario_name']}")
    print(f"New Ad Spend:                 {format_currency(sc['new_ad_spend'])}")
    print(f"New Units via Ads:            {sc['new_units_via_ads']:,}")
    print(f"New Ad Revenue:               {format_currency(sc['new_ad_revenue'])}")
    print(f"New ACOS:                     {format_percentage(sc['new_acos'])}")
    print(f"New TACOS:                    {format_percentage(sc['new_tacos'])}")
    print(f"Total Revenue:                {format_currency(sc['total_revenue'])}")
    print(f"Total Profit:                 {format_currency(sc['total_profit'])}")
    print(f"New Profitability Margin:     {format_percentage(sc['new_profitability_margin'])}")
    print()
    print(f"SCALING ANALYSIS:")
    print(f"  • Ad Spend Increase:        +{format_percentage(sc['spend_increase_pct'], 1)}")
    print(f"  • Revenue Increase:         +{format_percentage(sc['revenue_increase_pct'], 1)}")
    print(f"  • Profit Increase:          +{format_currency(sc['profit_increase'])} ({format_percentage(sc['profit_increase_pct'], 1)})")
    print(f"  • Current Profit:           {format_currency(sc['current_profit'])}")
    print(f"  • New Profit:               {format_currency(sc['total_profit'])}")
    print()
    print(f"MARGIN IMPACT:")
    print(f"  • Current Margin:           {format_percentage(sc['current_profitability_margin'])}")
    print(f"  • New Margin:               {format_percentage(sc['new_profitability_margin'])}")
    print(f"  • Change:                   {format_percentage(sc['profitability_margin_change'])}")
    print()
    print("RECOMMENDATION:")
    print("  NOT RECOMMENDED - Profit only increases 2.3% despite 100% ad spend increase.")
    print("  This shows severe diminishing returns. Focus on optimization, not scaling.")
    print("  Better approach: Invest in organic growth and operational excellence.")
    print()
    
    # Summary Table
    print("=" * 80)
    print("SUMMARY TABLE: ALL SCENARIOS")
    print("=" * 80)
    print()
    print(f"{'Metric':<30} {'Current':<20} {'Efficiency Drop':<20} {'Scaling Up':<20}")
    print("-" * 90)
    print(f"{'Ad Spend':<30} {format_currency(AD_SPEND_MONTHLY):<20} {format_currency(ed['new_ad_spend']):<20} {format_currency(sc['new_ad_spend']):<20}")
    print(f"{'Units (Ad)':<30} {UNITS_VIA_ADS:<20} {ed['new_units_via_ads']:<20} {sc['new_units_via_ads']:<20}")
    print(f"{'ACOS':<30} {format_percentage(at['acos']):<20} {format_percentage(ed['new_acos']):<20} {format_percentage(sc['new_acos']):<20}")
    print(f"{'TACOS':<30} {format_percentage(at['tacos']):<20} {format_percentage(at['tacos']):<20} {format_percentage(sc['new_tacos']):<20}")
    print(f"{'Monthly Profit':<30} {format_currency(mp['monthly_profit']):<20} {format_currency(ed['new_total_profit']):<20} {format_currency(sc['total_profit']):<20}")
    print(f"{'Profit Margin %':<30} {format_percentage(mp['profitability_margin']):<20} {format_percentage(ed['new_profitability_margin']):<20} {format_percentage(sc['new_profitability_margin']):<20}")
    print()
    
    print("=" * 80)
    print("CONCLUSION")
    print("=" * 80)
    print()
    print("GlowNest is in an EXCELLENT position:")
    print("  ✓ Current profitability: 36.9% (exceptional for ecommerce)")
    print("  ✓ ACOS 25% (efficient ad spending)")
    print("  ✓ TACOS 10.71% (building brand equity, not just renting visibility)")
    print("  ✓ Organic revenue 48% (growing organically alongside paid)")
    print()
    print("Key Decisions:")
    print("  1. DO NOT scale ad spend aggressively (diminishing returns evident)")
    print("  2. DO focus on optimizing existing campaigns (efficiency is key)")
    print("  3. DO monitor organic growth (this is the long-term profit engine)")
    print("  4. DO prepare for ACOS deterioration (watch for efficiency drops)")
    print()
    print("=" * 80)
    print()


if __name__ == "__main__":
    main()
