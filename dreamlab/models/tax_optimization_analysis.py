#!/usr/bin/env python3
"""
DreamLab AI Consulting - Tax Optimization Analysis
Ltd Company vs Sole Trader Structure Comparison
"""

import pandas as pd
import numpy as np
from typing import Dict, Tuple

class TaxOptimizationAnalysis:
    """Analyze optimal tax structure for DreamLab's dual revenue model"""
    
    def __init__(self):
        # Tax rates 2025/26
        self.tax_rates = {
            "personal_allowance": 12570,
            "basic_rate": 0.20,
            "basic_rate_threshold": 50270,
            "higher_rate": 0.40,
            "higher_rate_threshold": 125140,
            "additional_rate": 0.45,
            "ni_class_2": 3.45,  # Per week
            "ni_class_4_main": 0.09,
            "ni_class_4_additional": 0.02,
            "ni_threshold": 12570,
            "ni_upper": 50270,
            "corporation_tax": 0.19,
            "dividend_allowance": 500,
            "dividend_basic": 0.0875,
            "dividend_higher": 0.3375,
            "dividend_additional": 0.393
        }
        
        # Business projections (from main model)
        self.revenue_projections = {
            "year_1": {"training": 108000, "holiday": 42000, "gpu": 10000},
            "year_2": {"training": 162000, "holiday": 52000, "gpu": 15000},
            "year_3": {"training": 243000, "holiday": 58000, "gpu": 12000},
            "year_4": {"training": 324000, "holiday": 62000, "gpu": 8000},
            "year_5": {"training": 405000, "holiday": 65000, "gpu": 5000}
        }
        
        self.deductible_expenses = {
            "fixed_costs": 18000,
            "training_costs": 0.15,  # 15% of training revenue
            "holiday_costs": 0.25,   # 25% of holiday revenue
            "depreciation": 5000,
            "r_and_d_eligible": 25000
        }
        
    def calculate_sole_trader_tax(self, profit: float) -> Dict:
        """Calculate tax for sole trader structure"""
        # Class 2 NI
        class_2_ni = self.tax_rates["ni_class_2"] * 52
        
        # Class 4 NI
        if profit > self.tax_rates["ni_threshold"]:
            ni_main = min(profit - self.tax_rates["ni_threshold"], 
                         self.tax_rates["ni_upper"] - self.tax_rates["ni_threshold"]) * \
                         self.tax_rates["ni_class_4_main"]
            
            if profit > self.tax_rates["ni_upper"]:
                ni_additional = (profit - self.tax_rates["ni_upper"]) * \
                               self.tax_rates["ni_class_4_additional"]
            else:
                ni_additional = 0
            
            class_4_ni = ni_main + ni_additional
        else:
            class_4_ni = 0
        
        total_ni = class_2_ni + class_4_ni
        
        # Income tax
        if profit <= self.tax_rates["personal_allowance"]:
            income_tax = 0
        elif profit <= self.tax_rates["basic_rate_threshold"]:
            income_tax = (profit - self.tax_rates["personal_allowance"]) * \
                        self.tax_rates["basic_rate"]
        elif profit <= self.tax_rates["higher_rate_threshold"]:
            basic_tax = (self.tax_rates["basic_rate_threshold"] - 
                        self.tax_rates["personal_allowance"]) * self.tax_rates["basic_rate"]
            higher_tax = (profit - self.tax_rates["basic_rate_threshold"]) * \
                        self.tax_rates["higher_rate"]
            income_tax = basic_tax + higher_tax
        else:
            basic_tax = (self.tax_rates["basic_rate_threshold"] - 
                        self.tax_rates["personal_allowance"]) * self.tax_rates["basic_rate"]
            higher_tax = (self.tax_rates["higher_rate_threshold"] - 
                         self.tax_rates["basic_rate_threshold"]) * self.tax_rates["higher_rate"]
            additional_tax = (profit - self.tax_rates["higher_rate_threshold"]) * \
                            self.tax_rates["additional_rate"]
            income_tax = basic_tax + higher_tax + additional_tax
        
        total_tax = income_tax + total_ni
        net_income = profit - total_tax
        
        return {
            "profit": profit,
            "income_tax": income_tax,
            "class_2_ni": class_2_ni,
            "class_4_ni": class_4_ni,
            "total_tax": total_tax,
            "net_income": net_income,
            "effective_rate": (total_tax / profit * 100) if profit > 0 else 0
        }
    
    def calculate_ltd_tax(self, profit: float, salary: float, dividends: float) -> Dict:
        """Calculate tax for limited company structure"""
        # Corporation tax
        corp_tax = profit * self.tax_rates["corporation_tax"]
        
        # R&D tax credit
        r_and_d_credit = min(self.deductible_expenses["r_and_d_eligible"] * 0.186, corp_tax)
        net_corp_tax = corp_tax - r_and_d_credit
        
        # Profit after tax
        profit_after_tax = profit - net_corp_tax
        
        # Personal tax on salary
        salary_tax = self.calculate_sole_trader_tax(salary)
        
        # Dividend tax
        if dividends <= self.tax_rates["dividend_allowance"]:
            dividend_tax = 0
        else:
            taxable_dividends = dividends - self.tax_rates["dividend_allowance"]
            
            # Determine dividend tax rate based on total income
            total_income = salary + dividends
            
            if total_income <= self.tax_rates["basic_rate_threshold"]:
                dividend_tax = taxable_dividends * self.tax_rates["dividend_basic"]
            elif total_income <= self.tax_rates["higher_rate_threshold"]:
                # Some at basic, some at higher
                basic_portion = max(0, self.tax_rates["basic_rate_threshold"] - salary - 
                                  self.tax_rates["dividend_allowance"])
                higher_portion = taxable_dividends - basic_portion
                
                dividend_tax = (basic_portion * self.tax_rates["dividend_basic"] +
                              higher_portion * self.tax_rates["dividend_higher"])
            else:
                # Complex calculation for additional rate
                dividend_tax = taxable_dividends * self.tax_rates["dividend_higher"]
        
        # Total personal tax
        total_personal_tax = salary_tax["income_tax"] + salary_tax["class_2_ni"] + \
                           salary_tax["class_4_ni"] + dividend_tax
        
        # Net personal income
        net_personal_income = salary + dividends - total_personal_tax
        
        # Retained in company
        retained = profit_after_tax - dividends
        
        return {
            "profit": profit,
            "corporation_tax": net_corp_tax,
            "r_and_d_credit": r_and_d_credit,
            "profit_after_tax": profit_after_tax,
            "salary": salary,
            "dividends": dividends,
            "salary_tax": salary_tax["total_tax"],
            "dividend_tax": dividend_tax,
            "total_tax": net_corp_tax + total_personal_tax,
            "net_personal_income": net_personal_income,
            "retained_profits": retained,
            "effective_rate": ((net_corp_tax + total_personal_tax) / profit * 100) if profit > 0 else 0
        }
    
    def optimize_salary_dividend_split(self, profit: float) -> Tuple[float, float]:
        """Find optimal salary/dividend split for Ltd company"""
        # Optimal salary is usually around NI threshold
        optimal_salary = self.tax_rates["ni_threshold"]
        
        # Maximum dividends (leaving some for working capital)
        max_dividends = max(0, (profit - self.tax_rates["corporation_tax"] * profit) * 0.8)
        
        return optimal_salary, max_dividends
    
    def compare_structures(self) -> pd.DataFrame:
        """Compare tax efficiency across both structures over 5 years"""
        comparison_data = []
        
        for year in range(1, 6):
            # Calculate total revenue and profit
            revenue = sum(self.revenue_projections[f"year_{year}"].values())
            
            # Deductible expenses
            training_costs = self.revenue_projections[f"year_{year}"]["training"] * \
                           self.deductible_expenses["training_costs"]
            holiday_costs = self.revenue_projections[f"year_{year}"]["holiday"] * \
                          self.deductible_expenses["holiday_costs"]
            total_costs = (self.deductible_expenses["fixed_costs"] + 
                         training_costs + holiday_costs +
                         self.deductible_expenses["depreciation"])
            
            profit = revenue - total_costs
            
            # Sole trader calculation
            sole_trader = self.calculate_sole_trader_tax(profit)
            
            # Ltd company calculation with optimized split
            salary, dividends = self.optimize_salary_dividend_split(profit)
            ltd_company = self.calculate_ltd_tax(profit, salary, dividends)
            
            comparison_data.append({
                "Year": year,
                "Revenue": revenue,
                "Profit": profit,
                "Sole Trader Tax": sole_trader["total_tax"],
                "Sole Trader Net": sole_trader["net_income"],
                "Ltd Company Tax": ltd_company["total_tax"],
                "Ltd Company Net": ltd_company["net_personal_income"],
                "Ltd Retained": ltd_company["retained_profits"],
                "Tax Saving (Ltd)": sole_trader["total_tax"] - ltd_company["total_tax"],
                "Best Structure": "Ltd Company" if ltd_company["total_tax"] < sole_trader["total_tax"] else "Sole Trader"
            })
        
        return pd.DataFrame(comparison_data)
    
    def calculate_hybrid_approach(self) -> pd.DataFrame:
        """Analyze hybrid approach: Holiday let as sole trader, training as Ltd"""
        hybrid_data = []
        
        for year in range(1, 6):
            # Split revenues
            training_revenue = self.revenue_projections[f"year_{year}"]["training"]
            holiday_revenue = self.revenue_projections[f"year_{year}"]["holiday"]
            gpu_revenue = self.revenue_projections[f"year_{year}"]["gpu"]
            
            # Holiday let as sole trader (including GPU rental)
            holiday_costs = holiday_revenue * self.deductible_expenses["holiday_costs"]
            holiday_profit = holiday_revenue + gpu_revenue - holiday_costs - 5000  # Allocation of fixed costs
            sole_trader_tax = self.calculate_sole_trader_tax(holiday_profit)
            
            # Training as Ltd company
            training_costs = training_revenue * self.deductible_expenses["training_costs"]
            training_profit = training_revenue - training_costs - 13000  # Allocation of fixed costs
            
            salary, dividends = self.optimize_salary_dividend_split(training_profit)
            ltd_tax = self.calculate_ltd_tax(training_profit, salary, dividends)
            
            total_tax = sole_trader_tax["total_tax"] + ltd_tax["total_tax"]
            total_net = sole_trader_tax["net_income"] + ltd_tax["net_personal_income"]
            
            hybrid_data.append({
                "Year": year,
                "Holiday Let Profit": holiday_profit,
                "Holiday Let Tax": sole_trader_tax["total_tax"],
                "Training Profit": training_profit,
                "Training Tax": ltd_tax["total_tax"],
                "Total Tax": total_tax,
                "Total Net Income": total_net,
                "Retained in Ltd": ltd_tax["retained_profits"]
            })
        
        return pd.DataFrame(hybrid_data)
    
    def generate_tax_report(self) -> str:
        """Generate comprehensive tax optimization report"""
        comparison = self.compare_structures()
        hybrid = self.calculate_hybrid_approach()
        
        # 5-year totals
        sole_trader_total_tax = comparison["Sole Trader Tax"].sum()
        ltd_total_tax = comparison["Ltd Company Tax"].sum()
        hybrid_total_tax = hybrid["Total Tax"].sum()
        
        report = f"""
DREAMLAB TAX OPTIMIZATION ANALYSIS
=================================

5-YEAR TAX COMPARISON
--------------------
Sole Trader Total Tax: £{sole_trader_total_tax:,.0f}
Ltd Company Total Tax: £{ltd_total_tax:,.0f}
Hybrid Model Total Tax: £{hybrid_total_tax:,.0f}

Tax Savings (Ltd vs Sole): £{sole_trader_total_tax - ltd_total_tax:,.0f}
Tax Savings (Hybrid vs Sole): £{sole_trader_total_tax - hybrid_total_tax:,.0f}

YEAR-BY-YEAR ANALYSIS
--------------------
"""
        for idx, row in comparison.iterrows():
            report += f"""
Year {row['Year']}:
- Revenue: £{row['Revenue']:,.0f}
- Profit: £{row['Profit']:,.0f}
- Sole Trader: £{row['Sole Trader Tax']:,.0f} tax (£{row['Sole Trader Net']:,.0f} net)
- Ltd Company: £{row['Ltd Company Tax']:,.0f} tax (£{row['Ltd Company Net']:,.0f} net + £{row['Ltd Retained']:,.0f} retained)
- Recommended: {row['Best Structure']}
"""
        
        report += """
HYBRID MODEL BENEFITS
--------------------
Operating holiday let as sole trader while training business as Ltd provides:

1. Tax Efficiency:
   - Holiday let profits taxed as individual (mortgage interest relief available)
   - Training business benefits from R&D tax credits
   - Optimal use of personal allowances

2. Risk Segregation:
   - Training IP protected in Ltd company
   - Property risks isolated from business
   - Easier to scale or sell either component

3. Flexibility:
   - Can adjust salary/dividend mix annually
   - Holiday let losses offset against other income
   - Future pension contributions more flexible

RECOMMENDED STRUCTURE
--------------------
**Hybrid Model Implementation:**

1. Set up Ltd Company for:
   - AI training delivery
   - Consultancy services
   - IP ownership
   - R&D activities

2. Operate as Sole Trader for:
   - Holiday let income
   - GPU rental income
   - Property-related activities

3. Annual Optimization:
   - £12,570 salary from Ltd (NI threshold)
   - Dividends up to higher rate threshold
   - Pension contributions for tax relief
   - R&D tax credit claims

TAX PLANNING OPPORTUNITIES
-------------------------
1. Capital Allowances: 
   - 130% super-deduction on qualifying assets
   - Annual Investment Allowance on equipment

2. R&D Tax Credits:
   - 186% deduction on qualifying expenses
   - Cash credit if loss-making

3. Pension Contributions:
   - Up to £60,000 annual allowance
   - Corporation tax relief on employer contributions

4. Business Property Relief:
   - Potential IHT savings on business assets

IMPLEMENTATION TIMELINE
----------------------
Month 1-2: Incorporate Ltd company, register for taxes
Month 3: Set up accounting systems and segregation
Month 4+: Begin trading with optimized structure
Year End: Review and optimize based on actual figures
"""
        return report

# Run analysis
if __name__ == "__main__":
    tax_analysis = TaxOptimizationAnalysis()
    
    # Generate comparisons
    structure_comparison = tax_analysis.compare_structures()
    hybrid_analysis = tax_analysis.calculate_hybrid_approach()
    
    # Save data
    structure_comparison.to_csv("/workspace/dreamlab/financial-analysis/data/tax_structure_comparison.csv", index=False)
    hybrid_analysis.to_csv("/workspace/dreamlab/financial-analysis/data/hybrid_tax_analysis.csv", index=False)
    
    # Generate report
    report = tax_analysis.generate_tax_report()
    with open("/workspace/dreamlab/financial-analysis/reports/tax_optimization.txt", "w") as f:
        f.write(report)
    
    print(report)
    print("\nTax optimization analysis complete!")