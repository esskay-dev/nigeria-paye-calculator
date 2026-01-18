import streamlit as st
from tax import calculate_paye

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="Nigeria PAYE Tax Calculator",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ----------------------------------------------------
# CUSTOM STYLES (MOBILE FIRST)
# ----------------------------------------------------
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Metric cards */
[data-testid="metric-container"] {
    padding: 12px;
    border-radius: 12px;
    background-color: #f8f9fa;
}

/* Metric label */
[data-testid="metric-container"] label {
    font-size: 0.85rem;
}

/* Metric value */
[data-testid="metric-container"] div {
    font-size: 1.1rem;
    font-weight: 600;
}

/* Section headers */
h3 {
    font-size: 1.2rem;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------
st.title("Nigeria PAYE Tax Calculator")
st.caption("Calculate your PAYE tax using Nigeria's new tax rates")

st.divider()

# ----------------------------------------------------
# INPUT
# ----------------------------------------------------
salary_input = st.text_input(
    "Annual Income (₦)",
    placeholder="e.g. 1,000,000"
)

# ----------------------------------------------------
# TABS (BEST FOR MOBILE)
# ----------------------------------------------------
tabs = st.tabs(["Monthly Breakdown", "Annual Breakdown"])

with tabs[0]:
    monthly_income = st.metric("Monthly Income", "₦0.00")
    monthly_tax = st.metric("Monthly Tax", "₦0.00")
    monthly_net = st.metric("Monthly Net Income", "₦0.00")

with tabs[1]:
    annual_income = st.metric("Annual Income", "₦0.00")
    annual_tax = st.metric("Annual Tax", "₦0.00")
    annual_net = st.metric("Annual Net Income", "₦0.00")

st.divider()

# ----------------------------------------------------
# CALCULATE BUTTON
# ----------------------------------------------------
if st.button("Calculate PAYE", use_container_width=True):

    if salary_input.strip() == "":
        st.error("Please enter your annual income.")

    else:
        try:
            salary = float(salary_input.replace(",", ""))

            # Annual values
            annual_tax_val = calculate_paye(salary)
            annual_net_val = salary - annual_tax_val

            # Monthly values
            monthly_salary = salary / 12
            monthly_tax_val = annual_tax_val / 12
            monthly_net_val = monthly_salary - monthly_tax_val

            st.success("Calculation complete")

            # Update Monthly Tab
            with tabs[0]:
                st.metric("Monthly Income", f"₦{monthly_salary:,.2f}")
                st.metric("Monthly Tax", f"₦{monthly_tax_val:,.2f}")
                st.metric("Monthly Net Income", f"₦{monthly_net_val:,.2f}")

            # Update Annual Tab
            with tabs[1]:
                st.metric("Annual Income", f"₦{salary:,.2f}")
                st.metric("Annual Tax", f"₦{annual_tax_val:,.2f}")
                st.metric("Annual Net Income", f"₦{annual_net_val:,.2f}")

        except ValueError:
            st.error("Enter a valid amount (e.g. 1,000,000)")