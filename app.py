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
# HIDE STREAMLIT UI + MOBILE STYLES
# ----------------------------------------------------
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Metric card */
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

/* Headers */
h3 {
    font-size: 1.2rem;
}

/* Mobile */
@media (max-width: 768px) {
    [data-testid="metric-container"] div {
        font-size: 1rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------
st.title("Nigeria PAYE Tax Calculator")
st.caption("Mobile-friendly PAYE calculator using Nigeria's new tax rates")
st.divider()

# ----------------------------------------------------
# INPUT
# ----------------------------------------------------
salary_input = st.text_input(
    "Annual Income (₦)",
    placeholder="e.g. 1,000,000"
)

# ----------------------------------------------------
# LAYOUT: MONTHLY (LEFT) | ANNUAL (RIGHT)
# ----------------------------------------------------
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Monthly Breakdown")
    m_income = st.metric("Monthly Income", "₦0.00")
    m_tax = st.metric("Monthly Tax", "₦0.00")
    m_net = st.metric("Monthly Net Income", "₦0.00")

with right_col:
    st.subheader("Annual Breakdown")
    a_income = st.metric("Annual Income", "₦0.00")
    a_tax = st.metric("Annual Tax", "₦0.00")
    a_net = st.metric("Annual Net Income", "₦0.00")

st.divider()

# ----------------------------------------------------
# CALCULATE BUTTON
# ----------------------------------------------------
if st.button("Calculate PAYE", use_container_width=True):

    if not salary_input.strip():
        st.error("Please enter your annual income.")
    else:
        try:
            salary = float(salary_input.replace(",", ""))

            # Annual
            annual_tax = calculate_paye(salary)
            annual_net = salary - annual_tax

            # Monthly
            monthly_salary = salary / 12
            monthly_tax = annual_tax / 12
            monthly_net = monthly_salary - monthly_tax

            st.success("Calculation complete")

            # Update Monthly
            left_col.metric("Monthly Income", f"₦{monthly_salary:,.2f}")
            left_col.metric("Monthly Tax", f"₦{monthly_tax:,.2f}")
            left_col.metric("Monthly Net Income", f"₦{monthly_net:,.2f}")

            # Update Annual
            right_col.metric("Annual Income", f"₦{salary:,.2f}")
            right_col.metric("Annual Tax", f"₦{annual_tax:,.2f}")
            right_col.metric("Annual Net Income", f"₦{annual_net:,.2f}")

        except ValueError:
            st.error("Enter a valid amount (e.g. 1,000,000)")