import streamlit as st
from tax import calculate_paye

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------
st.set_page_config(
    page_title="Nigeria PAYE Tax Calculator",
    layout="centered"
)

# ----------------------------------------------------
# HIDE STREAMLIT DEFAULT UI + STYLE
# ----------------------------------------------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* Metric styling */
[data-testid="metric-container"] {
    padding: 12px;
    border-radius: 12px;
    background-color: #111827;
}

/* Metric label */
[data-testid="metric-container"] label {
    font-size: 0.85rem;
    color: #9ca3af;
}

/* Metric value */
[data-testid="metric-container"] div {
    font-size: 1.2rem;
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
st.caption("Calculate your PAYE tax using Nigeria’s new tax rates")

st.divider()

# ----------------------------------------------------
# INPUT
# ----------------------------------------------------
salary_input = st.text_input(
    "Annual Income (₦)",
    placeholder="e.g. 1,000,000"
)

st.divider()

# ----------------------------------------------------
# LAYOUT: MONTHLY (LEFT) | ANNUAL (RIGHT)
# ----------------------------------------------------
left_col, right_col = st.columns(2)

# MONTHLY
with left_col:
    st.subheader("Monthly Breakdown")
    m_income = st.empty()
    m_tax = st.empty()
    m_net = st.empty()

# ANNUAL
with right_col:
    st.subheader("Annual Breakdown")
    a_income = st.empty()
    a_tax = st.empty()
    a_net = st.empty()

# DEFAULT VALUES
m_income.metric("Monthly Income", "₦0.00")
m_tax.metric("Monthly Tax", "₦0.00")
m_net.metric("Monthly Net Income", "₦0.00")

a_income.metric("Annual Income", "₦0.00")
a_tax.metric("Annual Tax", "₦0.00")
a_net.metric("Annual Net Income", "₦0.00")

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

            # Annual calculations
            annual_tax = calculate_paye(salary)
            annual_net = salary - annual_tax

            # Monthly calculations
            monthly_salary = salary / 12
            monthly_tax = annual_tax / 12
            monthly_net = monthly_salary - monthly_tax

            # Update metrics
            m_income.metric("Monthly Income", f"₦{monthly_salary:,.2f}")
            m_tax.metric("Monthly Tax", f"₦{monthly_tax:,.2f}")
            m_net.metric("Monthly Net Income", f"₦{monthly_net:,.2f}")

            a_income.metric("Annual Income", f"₦{salary:,.2f}")
            a_tax.metric("Annual Tax", f"₦{annual_tax:,.2f}")
            a_net.metric("Annual Net Income", f"₦{annual_net:,.2f}")

        except ValueError:
            st.error("Enter a valid amount (e.g. 1,000,000)")