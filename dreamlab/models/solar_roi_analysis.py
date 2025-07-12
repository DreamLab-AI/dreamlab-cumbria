#!/usr/bin/env python3
"""
DreamLab AI Consulting - Solar Pergola ROI Analysis
6kW System with Battery Storage Financial Model
"""

import pandas as pd
import numpy as np

class SolarPergolROI:
    """Detailed ROI analysis for 6kW solar pergola installation"""
    
    def __init__(self):
        # System specifications
        self.system_specs = {
            "capacity_kw": 6.0,
            "annual_generation_kwh": 5400,  # Conservative for UK
            "battery_capacity_kwh": 13.5,   # Tesla Powerwall equivalent
            "system_efficiency": 0.85,      # Including inverter losses
            "degradation_rate": 0.005       # 0.5% per year
        }
        
        # Cost parameters
        self.costs = {
            "solar_panels": 6000,
            "pergola_structure": 4000,
            "inverter": 1500,
            "battery_storage": 8000,
            "installation": 2500,
            "total_capex": 22000,
            "annual_maintenance": 200,
            "insurance_increase": 150
        }
        
        # Financial parameters
        self.financial = {
            "electricity_rate_2025": 0.28,  # £/kWh
            "electricity_inflation": 0.05,   # 5% annual increase
            "feed_in_tariff": 0.055,        # SEG rate
            "discount_rate": 0.08,           # For NPV
            "system_lifetime": 25            # Years
        }
        
        # Usage patterns
        self.usage = {
            "base_consumption_kwh": 12000,   # Annual without EV/heat
            "gpu_consumption_kwh": 8760,     # 2x4090 GPUs
            "ev_charging_kwh": 3000,         # Future EV
            "heat_pump_kwh": 4000,           # Future heat pump
            "self_consumption_rate": 0.75     # With battery
        }
        
    def calculate_annual_savings(self) -> pd.DataFrame:
        """Calculate year-by-year savings from solar system"""
        years = range(1, self.financial["system_lifetime"] + 1)
        data = []
        
        for year in years:
            # Degraded generation
            generation = self.system_specs["annual_generation_kwh"] * \
                        (1 - self.system_specs["degradation_rate"]) ** (year - 1)
            
            # Electricity price with inflation
            elec_price = self.financial["electricity_rate_2025"] * \
                        (1 + self.financial["electricity_inflation"]) ** (year - 1)
            
            # Self-consumed electricity value
            self_consumed = generation * self.usage["self_consumption_rate"]
            self_consumed_value = self_consumed * elec_price
            
            # Exported electricity value
            exported = generation * (1 - self.usage["self_consumption_rate"])
            export_value = exported * self.financial["feed_in_tariff"]
            
            # Total savings
            total_savings = self_consumed_value + export_value
            
            # Operating costs
            maintenance = self.costs["annual_maintenance"] * (1.02 ** (year - 1))
            insurance = self.costs["insurance_increase"]
            operating_costs = maintenance + insurance
            
            # Net savings
            net_savings = total_savings - operating_costs
            
            data.append({
                "Year": year,
                "Generation (kWh)": int(generation),
                "Electricity Price": elec_price,
                "Self-Consumed Value": self_consumed_value,
                "Export Value": export_value,
                "Total Savings": total_savings,
                "Operating Costs": operating_costs,
                "Net Savings": net_savings
            })
        
        return pd.DataFrame(data)
    
    def calculate_battery_benefits(self) -> pd.DataFrame:
        """Calculate additional benefits from battery storage"""
        years = range(1, 11)  # 10-year battery warranty
        data = []
        
        for year in years:
            # Time-of-use arbitrage (charging overnight, using during peak)
            daily_arbitrage = 10  # kWh cycled daily
            peak_rate = 0.35 * (1.05 ** (year - 1))
            off_peak_rate = 0.15 * (1.05 ** (year - 1))
            
            arbitrage_savings = daily_arbitrage * 250 * (peak_rate - off_peak_rate)
            
            # Backup power value (avoided outage costs)
            outage_value = 500  # Annual value of backup power
            
            # Grid services potential
            grid_services = 300 * year  # Increasing as market develops
            
            total_battery_value = arbitrage_savings + outage_value + grid_services
            
            data.append({
                "Year": year,
                "Arbitrage Savings": arbitrage_savings,
                "Backup Value": outage_value,
                "Grid Services": grid_services,
                "Total Battery Value": total_battery_value
            })
        
        return pd.DataFrame(data)
    
    def calculate_business_benefits(self) -> Dict:
        """Calculate specific benefits for DreamLab business model"""
        benefits = {
            "gpu_cost_offset": {
                "annual_gpu_consumption": self.usage["gpu_consumption_kwh"],
                "solar_coverage": 0.40,  # 40% of GPU power from solar
                "annual_savings": self.usage["gpu_consumption_kwh"] * 0.40 * 0.28,
                "5_year_savings": self.usage["gpu_consumption_kwh"] * 0.40 * 0.28 * 5 * 1.25
            },
            "marketing_value": {
                "eco_premium": 0.10,  # 10% price premium for eco-credentials
                "training_revenue_boost": 108000 * 0.10,  # Year 1 training revenue
                "occupancy_boost": 0.05  # 5% occupancy increase
            },
            "resilience_value": {
                "avoided_downtime": 2000,  # Per year
                "data_protection": 1000,    # UPS functionality
                "total_annual": 3000
            }
        }
        return benefits
    
    def calculate_complete_roi(self) -> pd.DataFrame:
        """Calculate complete ROI including all benefits"""
        solar_savings = self.calculate_annual_savings()
        battery_benefits = self.calculate_battery_benefits()
        business_benefits = self.calculate_business_benefits()
        
        # Create comprehensive cash flow
        years = range(0, 26)
        cash_flows = []
        
        for year in years:
            if year == 0:
                # Initial investment
                cf = -self.costs["total_capex"]
            else:
                # Solar savings
                solar_cf = solar_savings.iloc[year-1]["Net Savings"] if year <= 25 else 0
                
                # Battery benefits (10 years)
                battery_cf = battery_benefits.iloc[year-1]["Total Battery Value"] if year <= 10 else 0
                
                # Business benefits
                gpu_savings = business_benefits["gpu_cost_offset"]["annual_savings"]
                marketing_value = business_benefits["marketing_value"]["training_revenue_boost"] * 0.2
                resilience = business_benefits["resilience_value"]["total_annual"]
                
                business_cf = gpu_savings + marketing_value + resilience
                
                # Battery replacement in year 10
                battery_replacement = -8000 if year == 10 else 0
                
                cf = solar_cf + battery_cf + business_cf + battery_replacement
            
            cash_flows.append({
                "Year": year,
                "Cash Flow": cf,
                "Cumulative": sum([c["Cash Flow"] for c in cash_flows[:year+1]])
            })
        
        return pd.DataFrame(cash_flows)
    
    def calculate_metrics(self) -> Dict:
        """Calculate key ROI metrics"""
        roi_df = self.calculate_complete_roi()
        cash_flows = roi_df["Cash Flow"].values
        
        # NPV
        npv = np.npv(self.financial["discount_rate"], cash_flows)
        
        # IRR
        try:
            irr = np.irr(cash_flows[:11])  # 10-year IRR
        except:
            irr = None
        
        # Payback period
        payback_idx = roi_df[roi_df["Cumulative"] > 0].index
        payback = payback_idx[0] if len(payback_idx) > 0 else ">25"
        
        # Total return
        total_return = sum(cash_flows[1:])
        roi_percent = (total_return / abs(cash_flows[0])) * 100
        
        # Carbon savings
        carbon_saved = sum(self.calculate_annual_savings()["Generation (kWh)"]) * 0.233 / 1000
        
        return {
            "Initial Investment": f"£{abs(cash_flows[0]):,.0f}",
            "NPV (8%)": f"£{npv:,.0f}",
            "IRR (10-year)": f"{irr*100:.1f}%" if irr else "N/A",
            "Payback Period": f"{payback} years",
            "25-Year Return": f"£{total_return:,.0f}",
            "ROI": f"{roi_percent:.0f}%",
            "Carbon Saved": f"{carbon_saved:.1f} tonnes CO2"
        }
    
    def generate_report(self) -> str:
        """Generate comprehensive solar ROI report"""
        metrics = self.calculate_metrics()
        annual = self.calculate_annual_savings()
        business = self.calculate_business_benefits()
        
        report = f"""
DREAMLAB SOLAR PERGOLA ROI ANALYSIS
==================================

SYSTEM SPECIFICATION
-------------------
- Capacity: 6kW solar PV system
- Battery: 13.5kWh storage system
- Annual Generation: 5,400 kWh (Year 1)
- Self-Consumption: 75% with battery

FINANCIAL METRICS
----------------
{chr(10).join(f'- {k}: {v}' for k, v in metrics.items())}

YEAR 1 BENEFITS BREAKDOWN
------------------------
- Electricity Savings: £{annual.iloc[0]['Self-Consumed Value']:,.0f}
- Export Income: £{annual.iloc[0]['Export Value']:,.0f}
- GPU Power Offset: £{business['gpu_cost_offset']['annual_savings']:,.0f}
- Business Resilience: £{business['resilience_value']['total_annual']:,.0f}
- Total Year 1 Benefit: £{annual.iloc[0]['Net Savings'] + business['gpu_cost_offset']['annual_savings'] + business['resilience_value']['total_annual']:,.0f}

STRATEGIC BENEFITS
-----------------
1. Energy Independence: 40% of GPU compute powered by solar
2. Marketing Advantage: Eco-credentials support premium pricing
3. Operational Resilience: Battery backup prevents downtime
4. Future-Proofing: Ready for EV charging and heat pump
5. Tax Benefits: Capital allowances on green technology

RISK MITIGATION
--------------
- 25-year panel warranty ensures long-term generation
- Battery storage maximizes self-consumption value
- Rising energy prices improve ROI over time
- System adds property value for future sale

RECOMMENDATION
-------------
The solar pergola investment delivers:
- Strong financial returns (NPV: {metrics['NPV (8%)']})
- Quick payback ({metrics['Payback Period']})
- Strategic business advantages
- Environmental leadership position

This investment aligns perfectly with DreamLab's premium positioning
and provides both immediate cost savings and long-term value creation.
"""
        return report

# Run analysis
if __name__ == "__main__":
    solar = SolarPergolROI()
    
    # Generate detailed tables
    annual_savings = solar.calculate_annual_savings()
    battery_benefits = solar.calculate_battery_benefits()
    complete_roi = solar.calculate_complete_roi()
    
    # Save to files
    annual_savings.to_csv("/workspace/dreamlab/financial-analysis/data/solar_annual_savings.csv", index=False)
    battery_benefits.to_csv("/workspace/dreamlab/financial-analysis/data/battery_benefits.csv", index=False)
    complete_roi.to_csv("/workspace/dreamlab/financial-analysis/data/solar_complete_roi.csv", index=False)
    
    # Generate report
    report = solar.generate_report()
    with open("/workspace/dreamlab/financial-analysis/reports/solar_roi_analysis.txt", "w") as f:
        f.write(report)
    
    print(report)
    print("\nSolar ROI analysis complete!")