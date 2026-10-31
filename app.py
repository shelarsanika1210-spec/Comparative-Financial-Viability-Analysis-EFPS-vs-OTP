import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Financial Viability - Sanika", page_icon="💰")

st.title("💰 Comparative Financial Viability Analysis")
st.subheader("EFPS (Eco-Friendly Packaging) vs OTP (Online Tutoring)")
st.markdown("**Author: Sanika Shelar | Financial Management Project 2025-26**")

# --- INPUTS ---
st.sidebar.header("💵 Investment Inputs")

efps_cost = st.sidebar.number_input("EFPS Initial Investment (₹)", value=500000)
otp_cost = st.sidebar.number_input("OTP Initial Investment (₹)", value=200000)

years = st.sidebar.slider("Years", 1, 10, 5)
discount = st.sidebar.slider("Discount Rate %", 1, 20, 10) / 100

st.sidebar.info("Values badal ke dekho, graph live change hoga!")

# Sample Cashflows
efps_cf = [120000, 150000, 180000, 200000, 220000][:years]
otp_cf = [80000, 100000, 120000, 130000, 150000][:years]

# NPV Calculation
def calc_npv(cost, cfs, r):
    npv = -cost
    for i, cf in enumerate(cfs):
        npv += cf / ((1+r)**(i+1))
    return npv

efps_npv = calc_npv(efps_cost, efps_cf, discount)
otp_npv = calc_npv(otp_cost, otp_cf, discount)

col1, col2 = st.columns(2)
col1.metric("EFPS NPV", f"₹ {efps_npv:,.0f}", delta="Viable" if efps_npv>0 else "Not Viable")
col2.metric("OTP NPV", f"₹ {otp_npv:,.0f}", delta="Viable" if otp_npv>0 else "Not Viable")

# Chart
fig, ax = plt.subplots()
ax.plot(range(1, years+1), efps_cf, marker='o', label='EFPS', linewidth=3)
ax.plot(range(1, years+1), otp_cf, marker='s', label='OTP', linewidth=3)
ax.set_xlabel("Year")
ax.set_ylabel("Cash Flow (₹)")
ax.set_title("Year-wise Cash Flow Comparison")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Table
df = pd.DataFrame({"Year": range(1, years+1), "EFPS Cashflow": efps_cf, "OTP Cashflow": otp_cf})
st.dataframe(df, use_container_width=True)

if efps_npv > otp_npv:
    st.success(f"✅ Recommendation: **EFPS is more viable** (Higher NPV)")
else:
    st.success(f"✅ Recommendation: **OTP is more viable** (Higher NPV)")

st.markdown("---")
st.caption("Made with ❤️ by Sanika Shelar | Deploy on Streamlit Cloud")