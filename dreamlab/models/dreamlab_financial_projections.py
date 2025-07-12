#!/usr/bin/env python3
"""
DreamLab AI Consulting - Comprehensive Financial Projections
Dual Revenue Model: AI Training + Luxury Holiday Let
Author: Financial Analyst Agent
Date: January 2025
"""

import pandas as pd
import numpy as np
from datetime import datetime, date
from typing import Dict, List, Tuple
import json

class DreamLabFinancialModel:
    """Complete financial model for DreamLab AI Consulting dual revenue streams"""
    
    def __init__(self):
        # Core financial parameters
        self.vat_rate = 0.20
        self.corporation_tax_rate = 0.19
        self.r_and_d_credit_rate = 0.186  # SME R&D tax credit
        self.discount_rate = 0.12  # For NPV calculations
        
        # Initial investment breakdown
        self.initial_investment = {
            "hardware": {
                "2x_4090_gpus": 4000,
                "high_spec_pc": 3000,
                "networking_equipment": 1500,
                "solar_pergola_6kw": 12000,
                "battery_storage": 8000,
                "total_hardware": 28500
            },
            "property_conversion": {
                "studio_conversion": 35000,
                "luxury_finishing": 15000,
                "professional_kitchen": 12000,
                "bathroom_upgrade": 8000,
                "insulation_heating": 6000,
                "total_conversion": 76000
            },
            "business_setup": {
                "legal_incorporation": 1000,
                "insurance_initial": 2500,
                "marketing_branding": 5000,
                "software_licenses": 3000,
                "contingency": 10000,
                "total_setup": 21500
            }
        }
        
        # Revenue parameters - Training
        self.training_params = {
            "price_per_delegate_per_day": 1500,
            "days_per_course": 3,
            "delegates_per_course": 3,
            "courses_year_1": 8,
            "courses_year_2": 12,
            "courses_year_3": 18,
            "courses_year_4": 24,
            "courses_year_5": 30,
            "course_growth_rate": 0.25
        }
        
        # Revenue parameters - Holiday Let
        self.holiday_let_params = {
            "peak_season_rate": 250,  # Per night
            "mid_season_rate": 180,
            "low_season_rate": 120,
            "peak_weeks": 12,  # Summer + Christmas
            "mid_weeks": 20,
            "low_weeks": 20,
            "occupancy_peak": 0.85,
            "occupancy_mid": 0.65,
            "occupancy_low": 0.45,
            "platform_commission": 0.15  # Airbnb/Booking.com
        }
        
        # GPU rental parameters
        self.gpu_rental_params = {
            "hourly_rate": 3.50,
            "available_hours_per_week": 100,  # When not training
            "utilization_rate": 0.60
        }
        
        # Operating costs
        self.operating_costs = {
            "fixed_annual": {
                "insurance": 3600,
                "business_rates": 2400,
                "utilities_base": 3600,
                "internet_premium": 1200,
                "software_subscriptions": 2400,
                "accounting": 1800,
                "maintenance": 3000,
                "total_fixed": 18000
            },
            "variable_training": {
                "catering_per_delegate_day": 80,
                "materials_per_delegate": 50,
                "electricity_per_day": 30
            },
            "variable_holiday": {
                "cleaning_per_stay": 60,
                "utilities_per_night": 15,
                "amenities_per_stay": 30
            }
        }
        
    def calculate_capital_investment(self) -> pd.DataFrame:
        """Calculate phased capital investment over 18 months"""
        phases = {
            "Phase 1 (Months 1-6)": {
                "Hardware": 15000,
                "Initial conversion": 30000,
                "Business setup": 10000,
                "Total": 55000
            },
            "Phase 2 (Months 7-12)": {
                "Remaining hardware": 13500,
                "Conversion completion": 30000,
                "Marketing launch": 5000,
                "Total": 48500
            },
            "Phase 3 (Months 13-18)": {
                "Final touches": 16000,
                "Contingency": 6500,
                "Total": 22500
            }
        }
        
        df = pd.DataFrame(phases).T
        df['Cumulative'] = df['Total'].cumsum()
        df['R&D Tax Credit'] = df['Total'] * 0.5 * self.r_and_d_credit_rate  # 50% qualifying
        
        return df
    
    def calculate_training_revenue(self) -> pd.DataFrame:
        """Calculate 5-year training revenue projections"""
        years = range(1, 6)
        data = []
        
        for year in years:
            if year == 1:
                courses = self.training_params["courses_year_1"]
            else:
                courses = int(self.training_params[f"courses_year_{year}"])
            
            revenue_per_course = (
                self.training_params["price_per_delegate_per_day"] *
                self.training_params["days_per_course"] *
                self.training_params["delegates_per_course"]
            )
            
            annual_revenue = courses * revenue_per_course
            
            # Variable costs
            catering_cost = (
                courses * self.training_params["delegates_per_course"] *
                self.training_params["days_per_course"] *
                self.operating_costs["variable_training"]["catering_per_delegate_day"]
            )
            
            materials_cost = (
                courses * self.training_params["delegates_per_course"] *
                self.operating_costs["variable_training"]["materials_per_delegate"]
            )
            
            electricity_cost = (
                courses * self.training_params["days_per_course"] *
                self.operating_costs["variable_training"]["electricity_per_day"]
            )
            
            total_costs = catering_cost + materials_cost + electricity_cost
            net_revenue = annual_revenue - total_costs
            
            data.append({
                "Year": year,
                "Courses": courses,
                "Delegates": courses * self.training_params["delegates_per_course"],
                "Training Days": courses * self.training_params["days_per_course"],
                "Gross Revenue": annual_revenue,
                "Variable Costs": total_costs,
                "Net Revenue": net_revenue,
                "Margin %": (net_revenue / annual_revenue * 100) if annual_revenue > 0 else 0
            })
        
        return pd.DataFrame(data)
    
    def calculate_holiday_let_revenue(self) -> pd.DataFrame:
        """Calculate 5-year holiday let revenue projections"""
        years = range(1, 6)
        data = []
        
        for year in years:
            # Year 1 starts with lower occupancy
            occupancy_factor = 0.7 if year == 1 else 1.0
            
            # Peak season revenue
            peak_nights = self.holiday_let_params["peak_weeks"] * 7
            peak_occupied = peak_nights * self.holiday_let_params["occupancy_peak"] * occupancy_factor
            peak_revenue = peak_occupied * self.holiday_let_params["peak_season_rate"]
            
            # Mid season revenue
            mid_nights = self.holiday_let_params["mid_weeks"] * 7
            mid_occupied = mid_nights * self.holiday_let_params["occupancy_mid"] * occupancy_factor
            mid_revenue = mid_occupied * self.holiday_let_params["mid_season_rate"]
            
            # Low season revenue
            low_nights = self.holiday_let_params["low_weeks"] * 7
            low_occupied = low_nights * self.holiday_let_params["occupancy_low"] * occupancy_factor
            low_revenue = low_occupied * self.holiday_let_params["low_season_rate"]
            
            # Total revenue and costs
            gross_revenue = peak_revenue + mid_revenue + low_revenue
            platform_fees = gross_revenue * self.holiday_let_params["platform_commission"]
            net_revenue = gross_revenue - platform_fees
            
            # Variable costs
            total_nights = peak_occupied + mid_occupied + low_occupied
            stays = total_nights / 3.5  # Average stay length
            
            cleaning_costs = stays * self.operating_costs["variable_holiday"]["cleaning_per_stay"]
            utilities_costs = total_nights * self.operating_costs["variable_holiday"]["utilities_per_night"]
            amenities_costs = stays * self.operating_costs["variable_holiday"]["amenities_per_stay"]
            
            total_costs = cleaning_costs + utilities_costs + amenities_costs
            net_profit = net_revenue - total_costs
            
            data.append({
                "Year": year,
                "Total Nights": int(total_nights),
                "Occupancy %": (total_nights / 365) * 100,
                "Gross Revenue": gross_revenue,
                "Platform Fees": platform_fees,
                "Variable Costs": total_costs,
                "Net Revenue": net_profit,
                "Margin %": (net_profit / gross_revenue * 100) if gross_revenue > 0 else 0
            })
        
        return pd.DataFrame(data)
    
    def calculate_gpu_rental_revenue(self) -> pd.DataFrame:
        """Calculate GPU rental revenue from excess compute capacity"""
        years = range(1, 6)
        data = []
        
        for year in years:
            # Available hours decrease as training increases
            training_days = [24, 36, 54, 72, 90][year-1]
            training_hours = training_days * 8  # 8 hours per training day
            
            total_hours = 52 * self.gpu_rental_params["available_hours_per_week"]
            available_hours = total_hours - training_hours
            
            utilized_hours = available_hours * self.gpu_rental_params["utilization_rate"]
            revenue = utilized_hours * self.gpu_rental_params["hourly_rate"]
            
            # Minimal variable costs for GPU rental
            electricity_cost = utilized_hours * 0.50  # £0.50 per hour electricity
            
            data.append({
                "Year": year,
                "Available Hours": int(available_hours),
                "Utilized Hours": int(utilized_hours),
                "Revenue": revenue,
                "Electricity Cost": electricity_cost,
                "Net Revenue": revenue - electricity_cost,
                "Margin %": ((revenue - electricity_cost) / revenue * 100) if revenue > 0 else 0
            })
        
        return pd.DataFrame(data)
    
    def calculate_consolidated_pnl(self) -> pd.DataFrame:
        """Create consolidated P&L for 5 years"""
        training = self.calculate_training_revenue()
        holiday = self.calculate_holiday_let_revenue()
        gpu = self.calculate_gpu_rental_revenue()
        
        years = range(1, 6)
        data = []
        
        for year in years:
            idx = year - 1
            
            # Revenue streams
            training_revenue = training.iloc[idx]["Net Revenue"]
            holiday_revenue = holiday.iloc[idx]["Net Revenue"]
            gpu_revenue = gpu.iloc[idx]["Net Revenue"]
            total_revenue = training_revenue + holiday_revenue + gpu_revenue
            
            # Fixed costs
            fixed_costs = self.operating_costs["fixed_annual"]["total_fixed"]
            
            # EBITDA
            ebitda = total_revenue - fixed_costs
            
            # Depreciation (20% on hardware)
            depreciation = self.initial_investment["hardware"]["total_hardware"] * 0.20
            
            # Interest (if any loan)
            interest = 0  # Assuming no debt
            
            # Pre-tax profit
            pre_tax_profit = ebitda - depreciation - interest
            
            # Tax calculation (simplified)
            if pre_tax_profit > 0:
                tax = pre_tax_profit * self.corporation_tax_rate
                # R&D tax credit (first 3 years)
                if year <= 3:
                    r_and_d_credit = 25000  # Estimated annual R&D spending * credit rate
                    tax = max(0, tax - r_and_d_credit)
            else:
                tax = 0
            
            net_profit = pre_tax_profit - tax
            
            data.append({
                "Year": year,
                "Training Revenue": training_revenue,
                "Holiday Let Revenue": holiday_revenue,
                "GPU Rental Revenue": gpu_revenue,
                "Total Revenue": total_revenue,
                "Fixed Costs": fixed_costs,
                "EBITDA": ebitda,
                "Depreciation": depreciation,
                "Interest": interest,
                "Pre-tax Profit": pre_tax_profit,
                "Tax": tax,
                "Net Profit": net_profit,
                "Net Margin %": (net_profit / total_revenue * 100) if total_revenue > 0 else 0
            })
        
        return pd.DataFrame(data)
    
    def calculate_cash_flow(self) -> pd.DataFrame:
        """Calculate cash flow projections"""
        pnl = self.calculate_consolidated_pnl()
        capital = self.calculate_capital_investment()
        
        # Initial investment
        initial_outflow = -self.initial_investment["hardware"]["total_hardware"] - \
                         self.initial_investment["property_conversion"]["total_conversion"] - \
                         self.initial_investment["business_setup"]["total_setup"]
        
        cash_flows = [initial_outflow]
        
        for year in range(1, 6):
            idx = year - 1
            
            # Operating cash flow
            net_profit = pnl.iloc[idx]["Net Profit"]
            depreciation = pnl.iloc[idx]["Depreciation"]
            operating_cf = net_profit + depreciation
            
            # Working capital changes (simplified)
            wc_change = -pnl.iloc[idx]["Total Revenue"] * 0.05 if year == 1 else 0
            
            # Capital expenditure (replacement after year 3)
            capex = -10000 if year == 3 else 0
            
            # R&D tax credit recovery
            r_and_d_recovery = 25000 * self.r_and_d_credit_rate if year <= 3 else 0
            
            total_cf = operating_cf + wc_change + capex + r_and_d_recovery
            cash_flows.append(total_cf)
        
        # Calculate cumulative cash flow
        cum_cf = np.cumsum(cash_flows)
        
        # Create DataFrame
        cf_data = pd.DataFrame({
            "Year": range(0, 6),
            "Cash Flow": cash_flows,
            "Cumulative CF": cum_cf
        })
        
        return cf_data
    
    def calculate_financial_metrics(self) -> Dict:
        """Calculate key financial metrics"""
        cf = self.calculate_cash_flow()
        cash_flows = cf["Cash Flow"].values
        
        # NPV calculation
        npv = np.npv(self.discount_rate, cash_flows)
        
        # IRR calculation
        try:
            irr = np.irr(cash_flows) * 100
        except:
            irr = None
        
        # Payback period
        cumulative = cf["Cumulative CF"].values
        payback_idx = np.where(cumulative > 0)[0]
        if len(payback_idx) > 0:
            payback_period = payback_idx[0]
        else:
            payback_period = ">5 years"
        
        # ROI calculation
        total_investment = abs(cash_flows[0])
        total_return = sum(cash_flows[1:])
        roi = (total_return / total_investment) * 100
        
        return {
            "NPV": f"£{npv:,.0f}",
            "IRR": f"{irr:.1f}%" if irr else "N/A",
            "Payback Period": f"{payback_period} years" if isinstance(payback_period, int) else payback_period,
            "ROI": f"{roi:.1f}%",
            "Total Investment": f"£{total_investment:,.0f}",
            "5-Year Return": f"£{total_return:,.0f}"
        }
    
    def sensitivity_analysis(self) -> pd.DataFrame:
        """Perform sensitivity analysis on key variables"""
        base_npv = np.npv(self.discount_rate, self.calculate_cash_flow()["Cash Flow"].values)
        
        scenarios = []
        
        # Training price sensitivity
        for price_change in [-20, -10, 0, 10, 20]:
            self.training_params["price_per_delegate_per_day"] = 1500 * (1 + price_change/100)
            cf = self.calculate_cash_flow()
            npv = np.npv(self.discount_rate, cf["Cash Flow"].values)
            scenarios.append({
                "Variable": "Training Price",
                "Change %": price_change,
                "NPV": npv,
                "Impact %": ((npv - base_npv) / base_npv) * 100
            })
        
        # Reset
        self.training_params["price_per_delegate_per_day"] = 1500
        
        # Occupancy sensitivity
        for occ_change in [-20, -10, 0, 10, 20]:
            factor = 1 + occ_change/100
            self.holiday_let_params["occupancy_peak"] = 0.85 * factor
            self.holiday_let_params["occupancy_mid"] = 0.65 * factor
            self.holiday_let_params["occupancy_low"] = 0.45 * factor
            
            cf = self.calculate_cash_flow()
            npv = np.npv(self.discount_rate, cf["Cash Flow"].values)
            scenarios.append({
                "Variable": "Holiday Occupancy",
                "Change %": occ_change,
                "NPV": npv,
                "Impact %": ((npv - base_npv) / base_npv) * 100
            })
        
        return pd.DataFrame(scenarios)
    
    def generate_summary_report(self) -> str:
        """Generate executive summary of financial projections"""
        metrics = self.calculate_financial_metrics()
        pnl = self.calculate_consolidated_pnl()
        
        report = f"""
DREAMLAB AI CONSULTING - FINANCIAL PROJECTIONS EXECUTIVE SUMMARY
================================================================

INVESTMENT OVERVIEW
------------------
Total Capital Required: {metrics['Total Investment']}
- Hardware & Solar: £28,500
- Property Conversion: £76,000
- Business Setup: £21,500

REVENUE PROJECTIONS (5 YEARS)
----------------------------
Year 1 Revenue: £{pnl.iloc[0]['Total Revenue']:,.0f}
Year 5 Revenue: £{pnl.iloc[4]['Total Revenue']:,.0f}
CAGR: {((pnl.iloc[4]['Total Revenue']/pnl.iloc[0]['Total Revenue'])**(1/4)-1)*100:.1f}%

Revenue Mix (Year 5):
- AI Training: £{pnl.iloc[4]['Training Revenue']:,.0f} ({pnl.iloc[4]['Training Revenue']/pnl.iloc[4]['Total Revenue']*100:.0f}%)
- Holiday Let: £{pnl.iloc[4]['Holiday Let Revenue']:,.0f} ({pnl.iloc[4]['Holiday Let Revenue']/pnl.iloc[4]['Total Revenue']*100:.0f}%)
- GPU Rental: £{pnl.iloc[4]['GPU Rental Revenue']:,.0f} ({pnl.iloc[4]['GPU Rental Revenue']/pnl.iloc[4]['Total Revenue']*100:.0f}%)

PROFITABILITY
-------------
Year 1 Net Profit: £{pnl.iloc[0]['Net Profit']:,.0f} ({pnl.iloc[0]['Net Margin %']:.1f}% margin)
Year 5 Net Profit: £{pnl.iloc[4]['Net Profit']:,.0f} ({pnl.iloc[4]['Net Margin %']:.1f}% margin)

KEY FINANCIAL METRICS
--------------------
NPV @ 12%: {metrics['NPV']}
IRR: {metrics['IRR']}
Payback Period: {metrics['Payback Period']}
5-Year ROI: {metrics['ROI']}

RISK MITIGATION
--------------
- Dual revenue streams reduce dependency
- Solar installation reduces operating costs
- R&D tax credits offset initial investment
- Premium positioning ensures margin protection
"""
        return report

# Create and test the model
if __name__ == "__main__":
    model = DreamLabFinancialModel()
    
    # Generate all reports
    print("Generating financial projections...")
    
    # Save detailed projections
    training_rev = model.calculate_training_revenue()
    holiday_rev = model.calculate_holiday_let_revenue()
    gpu_rev = model.calculate_gpu_rental_revenue()
    consolidated = model.calculate_consolidated_pnl()
    cash_flow = model.calculate_cash_flow()
    sensitivity = model.sensitivity_analysis()
    
    # Save to CSV files
    training_rev.to_csv("/workspace/dreamlab/financial-analysis/data/training_revenue.csv", index=False)
    holiday_rev.to_csv("/workspace/dreamlab/financial-analysis/data/holiday_revenue.csv", index=False)
    gpu_rev.to_csv("/workspace/dreamlab/financial-analysis/data/gpu_revenue.csv", index=False)
    consolidated.to_csv("/workspace/dreamlab/financial-analysis/data/consolidated_pnl.csv", index=False)
    cash_flow.to_csv("/workspace/dreamlab/financial-analysis/data/cash_flow.csv", index=False)
    sensitivity.to_csv("/workspace/dreamlab/financial-analysis/data/sensitivity_analysis.csv", index=False)
    
    # Generate and save summary
    summary = model.generate_summary_report()
    with open("/workspace/dreamlab/financial-analysis/reports/executive_summary.txt", "w") as f:
        f.write(summary)
    
    print(summary)
    print("\nAll financial projections saved to dreamlab/financial-analysis/")