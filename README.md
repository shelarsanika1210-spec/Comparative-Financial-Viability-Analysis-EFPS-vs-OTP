# Comparative Financial Viability Analysis - EFPS vs OTP
# Author: Sanika Shelar | Financial Management | Python
# Academic Year: 2025

import numpy as np
import matplotlib.pyplot as plt

# ==============================
# A. PROJECT DATA (Rs. in Lakhs)
# ==============================
years = np.array([1, 2, 3, 4, 5])

eco_packaging = np.array([3.4, 6.0, 9.0, 12.0, 16.0])      # EFPS
online_tutoring = np.array([1.9, 3.5, 5.0, 6.0, 7.5])      # OTP

initial_investment = {
    'Eco-Friendly Packaging': 15.0,
    'Online Tutoring': 5.0
}
discount_rate = 0.12

# ==============================
# B. NPV CALCULATION
# ==============================
def calculate_npv(cash_flows, initial, rate):
    pv = sum(cf / ((1 + rate) ** (i+1)) for i, cf in enumerate(cash_flows))
    return pv - initial

npv_eco = calculate_npv(eco_packaging, 15.0, discount_rate)
npv_tutoring = calculate_npv(online_tutoring, 5.0, discount_rate)

print("="*50)
print("FINANCIAL VIABILITY ANALYSIS")
print("="*50)
print(f"NPV Eco-Friendly Packaging: Rs. {npv_eco:.2f} Lakhs")
print(f"NPV Online Tutoring: Rs. {npv_tutoring:.2f} Lakhs")

# ==============================
# C. GRAPH - Figure A.1
# ==============================
plt.figure(figsize=(10, 6))
plt.plot(years, eco_packaging, marker='o', linewidth=2.5, label='Eco-Friendly Packaging', color='#1f77b4')
plt.plot(years, online_tutoring, marker='s', linewidth=2.5, label='Online Tutoring', color='#ff7f0e')
plt.title('Projected Net Cash Flows Comparison (Rs. in Lakhs)', fontsize=14, fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Cash Flow (Lakhs)')
plt.xticks(years)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig('cashflow.png', dpi=300)  # Ye image README me use hogi
plt.show()