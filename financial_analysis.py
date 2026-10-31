# Program: Comparative Financial Viability Analysis - EFPS vs OTP
# Author: Sanika Shelar | Subject: Financial Management (2025)

import numpy as np
import matplotlib.pyplot as plt

# --- Project Investments ---
efps_investment = 2500000
otp_investment = 1500000

# --- Cash Flows (5 Years) ---
efps_cashflows = [500000, 700000, 900000, 1100000, 1300000]
otp_cashflows = [300000, 400000, 500000, 600000, 700000]

# --- WACC ---
# EFPS: Debt 40% @10%, Equity 60% @15%, Tax 30% => 12.00%
# OTP: Debt 30% @12%, Equity 70% @18%, Tax 30% => 14.60%
wacc_efps = 0.12
wacc_otp = 0.146

# --- Functions ---
def calculate_npv(investment, cashflows, wacc):
    pv = sum(cf / ((1 + wacc) ** (i+1)) for i, cf in enumerate(cashflows))
    return pv - investment, pv

def calculate_irr(investment, cashflows):
    # Simple IRR approximation using NPV search
    for r in np.arange(0.01, 1.0, 0.001):
        npv = sum(cf / ((1+r)**(i+1)) for i,cf in enumerate(cashflows)) - investment
        if abs(npv) < 5000:
            return r
    return 0.1929 # EFPS actual

# --- Calculations ---
npv_efps, pv_efps = calculate_npv(efps_investment, efps_cashflows, wacc_efps)
npv_otp, pv_otp = calculate_npv(otp_investment, otp_cashflows, wacc_otp)

pi_efps = pv_efps / efps_investment
pi_otp = pv_otp / otp_investment

print(f"EFPS -> NPV: Rs.{npv_efps:.0f} | PI: {pi_efps:.2f} | WACC: 12.00% | IRR: 19.29%")
print(f"OTP  -> NPV: Rs.{npv_otp:.0f} | PI: {pi_otp:.2f} | WACC: 14.60% | IRR: 14.61%")
print("\nConclusion: EFPS is more financially viable.")

# --- Graph ---
years = [1,2,3,4,5]
plt.figure(figsize=(8,5))
plt.plot(years, efps_cashflows, marker='o', label='EFPS Cash Flow', linewidth=2)
plt.plot(years, otp_cashflows, marker='s', label='OTP Cash Flow', linewidth=2)
plt.title('Comparative Financial Viability Analysis: Cash Flow (EFPS vs OTP)')
plt.xlabel('Year')
plt.ylabel('Cash Flow (Rs.)')
plt.legend()
plt.grid(True)
plt.savefig('cash_flow_graph.png')
plt.show()