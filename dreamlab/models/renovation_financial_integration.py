#!/usr/bin/env python3
"""
Fairfield House Renovation Financial Integration
Integrates house renovation costs with DreamLab business financial model
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

class RenovationFinancialModel:
    def __init__(self):
        # Renovation cost data from estimates
        self.renovation_costs = {
            'phase_1': {
                'items': ['Trifold doors', 'Kitchen refit', 'Triple glazed window'],
                'months': [4, 5, 6],  # Apr-Jun 2025
                'costs_low': [25000, 15000, 1200],
                'costs_high': [40000, 25000, 1700]
            },
            'phase_2': {
                'items': ['Chimney/fire', 'Luxury shower', 'Battery storage', 'Trim & finishes'],
                'months': [7, 8, 9, 9],  # Jul-Sep 2025
                'costs_low': [3500, 12000, 10795, 2000],
                'costs_high': [5500, 20000, 11100, 3500]
            },
            'phase_3': {
                'items': ['Solar pergola x3', 'Garden clearing', 'Shed/woodstore'],
                'months': [16, 16, 17],  # Apr-Jun 2026
                'costs_low': [22200, 1500, 2000],
                'costs_high': [22200, 3000, 4000]
            },
            'phase_4': {
                'items': ['Outdoor sauna', 'Trampoline pit', 'Shelving units', 'Rabbit hutch'],
                'months': [20, 19, 21, 21],  # Jul-Sep 2026
                'costs_low': [12160, 2500, 2000, 500],
                'costs_high': [17160, 4000, 3500, 1000]
            }
        }
        
        # Lab/training costs (separate budget)
        self.lab_costs = {
            'low': 125000,
            'high': 136000,
            'start_month': 13,  # Jan 2026
            'duration': 9  # 9 months
        }
        
        # Business revenue projections (from existing model)
        self.revenue_projections = {
            'training': {
                'year_1': {'courses': 8, 'delegates': 24, 'revenue': 108000, 'margin': 0.85},
                'year_2': {'courses': 12, 'delegates': 36, 'revenue': 162000, 'margin': 0.85},
                'year_3': {'courses': 18, 'delegates': 54, 'revenue': 243000, 'margin': 0.85},
                'year_4': {'courses': 24, 'delegates': 72, 'revenue': 324000, 'margin': 0.85},
                'year_5': {'courses': 30, 'delegates': 90, 'revenue': 405000, 'margin': 0.85}
            },
            'holiday_let': {
                'year_1': {'occupancy': 0.52, 'nights': 190, 'revenue': 42000, 'margin': 0.75},
                'year_2': {'occupancy': 0.65, 'nights': 237, 'revenue': 52000, 'margin': 0.75},
                'year_3': {'occupancy': 0.68, 'nights': 248, 'revenue': 58000, 'margin': 0.75},
                'year_4': {'occupancy': 0.70, 'nights': 256, 'revenue': 62000, 'margin': 0.75},
                'year_5': {'occupancy': 0.72, 'nights': 263, 'revenue': 65000, 'margin': 0.75}
            },
            'gpu_rental': {
                'year_1': {'hours': 4968, 'revenue': 10416, 'margin': 0.95},
                'year_2': {'hours': 4680, 'revenue': 9828, 'margin': 0.95},
                'year_3': {'hours': 4248, 'revenue': 8920, 'margin': 0.95},
                'year_4': {'hours': 3672, 'revenue': 7711, 'margin': 0.95},
                'year_5': {'hours': 3000, 'revenue': 6300, 'margin': 0.95}
            }
        }
        
    def calculate_monthly_cashflow(self, scenario='base'):
        """Calculate monthly cashflow including renovation costs"""
        months = 60  # 5 years
        cashflow = pd.DataFrame(index=range(months))
        cashflow['month'] = cashflow.index + 1
        cashflow['year'] = (cashflow['month'] - 1) // 12 + 1
        cashflow['month_in_year'] = (cashflow['month'] - 1) % 12 + 1
        
        # Initialize columns
        cashflow['renovation_costs'] = 0
        cashflow['lab_costs'] = 0
        cashflow['training_revenue'] = 0
        cashflow['holiday_revenue'] = 0
        cashflow['gpu_revenue'] = 0
        cashflow['total_revenue'] = 0
        cashflow['operating_costs'] = 0
        cashflow['net_cashflow'] = 0
        cashflow['cumulative_cashflow'] = 0
        
        # Apply renovation costs
        cost_multiplier = 1.0 if scenario == 'low' else 1.5 if scenario == 'high' else 1.25
        
        for phase, data in self.renovation_costs.items():
            for i, month in enumerate(data['months']):
                if month <= months:
                    if scenario == 'low':
                        cost = data['costs_low'][i]
                    elif scenario == 'high':
                        cost = data['costs_high'][i]
                    else:  # base case
                        cost = (data['costs_low'][i] + data['costs_high'][i]) / 2
                    cashflow.loc[month-1, 'renovation_costs'] = cost
        
        # Apply lab costs (spread over duration)
        lab_monthly = self.lab_costs[scenario if scenario in ['low', 'high'] else 'low'] / self.lab_costs['duration']
        for month in range(self.lab_costs['start_month'], self.lab_costs['start_month'] + self.lab_costs['duration']):
            if month <= months:
                cashflow.loc[month-1, 'lab_costs'] = lab_monthly
        
        # Apply revenues (starting from month 25 - Jan 2027)
        revenue_start = 25
        for month in range(revenue_start-1, months):
            year_offset = (month - revenue_start + 1) // 12 + 1
            if year_offset <= 5:
                # Training revenue (monthly average)
                year_key = f'year_{year_offset}'
                cashflow.loc[month, 'training_revenue'] = self.revenue_projections['training'][year_key]['revenue'] / 12
                cashflow.loc[month, 'holiday_revenue'] = self.revenue_projections['holiday_let'][year_key]['revenue'] / 12
                cashflow.loc[month, 'gpu_revenue'] = self.revenue_projections['gpu_rental'][year_key]['revenue'] / 12
        
        # Calculate totals
        cashflow['total_revenue'] = cashflow['training_revenue'] + cashflow['holiday_revenue'] + cashflow['gpu_revenue']
        cashflow['total_costs'] = cashflow['renovation_costs'] + cashflow['lab_costs']
        cashflow['operating_costs'] = cashflow['total_revenue'] * 0.20  # 20% operating costs
        cashflow['net_cashflow'] = cashflow['total_revenue'] - cashflow['total_costs'] - cashflow['operating_costs']
        cashflow['cumulative_cashflow'] = cashflow['net_cashflow'].cumsum()
        
        return cashflow
    
    def calculate_roi_metrics(self, cashflow):
        """Calculate ROI metrics including payback period and IRR"""
        # Find payback period
        positive_cumulative = cashflow[cashflow['cumulative_cashflow'] > 0]
        if len(positive_cumulative) > 0:
            payback_months = positive_cumulative.index[0] + 1
            payback_years = payback_months / 12
        else:
            payback_years = None
        
        # Calculate IRR
        cash_flows = cashflow['net_cashflow'].values
        try:
            irr_monthly = np.irr(cash_flows)
            irr_annual = (1 + irr_monthly) ** 12 - 1
        except:
            irr_annual = None
        
        # Calculate NPV at 12% discount rate
        discount_rate_monthly = 0.12 / 12
        months = np.arange(len(cashflow))
        discount_factors = (1 + discount_rate_monthly) ** -months
        npv = np.sum(cash_flows * discount_factors)
        
        # Total investment
        total_investment = cashflow['renovation_costs'].sum() + cashflow['lab_costs'].sum()
        
        # 5-year profit
        total_profit = cashflow['net_cashflow'].sum()
        
        # ROI
        roi = (total_profit / total_investment * 100) if total_investment > 0 else None
        
        return {
            'payback_years': payback_years,
            'irr_annual': irr_annual,
            'npv': npv,
            'total_investment': total_investment,
            'total_profit': total_profit,
            'roi_percentage': roi
        }
    
    def generate_comparison_analysis(self):
        """Compare Airbnb-only vs Training+Airbnb models"""
        # Airbnb-only scenario (full property, higher occupancy)
        airbnb_only = {
            'year_1': {'occupancy': 0.65, 'nightly_rate': 350, 'annual_revenue': 83000},
            'year_2': {'occupancy': 0.70, 'nightly_rate': 350, 'annual_revenue': 89000},
            'year_3': {'occupancy': 0.72, 'nightly_rate': 360, 'annual_revenue': 95000},
            'year_4': {'occupancy': 0.72, 'nightly_rate': 370, 'annual_revenue': 97000},
            'year_5': {'occupancy': 0.72, 'nightly_rate': 380, 'annual_revenue': 100000}
        }
        
        # Training+Airbnb model (from projections)
        training_model = {
            'year_1': {'total_revenue': 160416, 'training': 108000, 'holiday': 42000, 'gpu': 10416},
            'year_2': {'total_revenue': 223828, 'training': 162000, 'holiday': 52000, 'gpu': 9828},
            'year_3': {'total_revenue': 309920, 'training': 243000, 'holiday': 58000, 'gpu': 8920},
            'year_4': {'total_revenue': 393711, 'training': 324000, 'holiday': 62000, 'gpu': 7711},
            'year_5': {'total_revenue': 476300, 'training': 405000, 'holiday': 65000, 'gpu': 6300}
        }
        
        comparison = pd.DataFrame()
        for year in range(1, 6):
            year_key = f'year_{year}'
            comparison.loc[year, 'airbnb_only_revenue'] = airbnb_only[year_key]['annual_revenue']
            comparison.loc[year, 'training_model_revenue'] = training_model[year_key]['total_revenue']
            comparison.loc[year, 'revenue_difference'] = training_model[year_key]['total_revenue'] - airbnb_only[year_key]['annual_revenue']
            comparison.loc[year, 'percentage_increase'] = (comparison.loc[year, 'revenue_difference'] / airbnb_only[year_key]['annual_revenue'] * 100)
        
        return comparison
    
    def save_analysis(self):
        """Save all analysis to files"""
        # Calculate for all scenarios
        scenarios = ['low', 'base', 'high']
        results = {}
        
        for scenario in scenarios:
            cashflow = self.calculate_monthly_cashflow(scenario)
            metrics = self.calculate_roi_metrics(cashflow)
            results[scenario] = {
                'metrics': metrics,
                'monthly_cashflow': cashflow.to_dict('records')
            }
        
        # Save results
        with open('/workspace/ext/dreamlab/data/renovation_integration_results.json', 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        # Save comparison
        comparison = self.generate_comparison_analysis()
        comparison.to_csv('/workspace/ext/dreamlab/data/airbnb_vs_training_comparison.csv')
        
        # Save summary cashflow
        base_cashflow = self.calculate_monthly_cashflow('base')
        base_cashflow.to_csv('/workspace/ext/dreamlab/data/integrated_cashflow_monthly.csv')
        
        return results

if __name__ == '__main__':
    model = RenovationFinancialModel()
    results = model.save_analysis()
    
    print("Renovation Financial Integration Complete")
    print("\nBase Case Metrics:")
    for key, value in results['base']['metrics'].items():
        if value is not None:
            if key in ['npv', 'total_investment', 'total_profit']:
                print(f"{key}: £{value:,.0f}")
            elif key == 'payback_years':
                print(f"{key}: {value:.1f} years")
            elif key == 'irr_annual':
                print(f"{key}: {value:.1%}")
            elif key == 'roi_percentage':
                print(f"{key}: {value:.0f}%")