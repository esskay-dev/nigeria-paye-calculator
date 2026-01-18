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
# STYLES
# ----------------------------------------------------
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Metric cards */
    [data-testid="metric-container"] {
        padding: 12px;
        border-radius: 12px;
        background-color: #0f172a;
    }

    [data-testid="metric-container"] label {
        font-size: 0.8rem;
        color: #cbd5f5;
    }

    [data-testid="metric-container"] div {
        font-size: 1.05rem;
        font-weight: 600;
        color: white;
    }

    h3 {
        font-size: 1.15rem;
    }

    @media (max-width: 768px) {
        [data-testid="metric-container"] div {
            font-size: 1rem;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------
st.title("Nigeria PAYE Tax Calculator")
st.caption("Calculate your PAYE based on Nigeria’s new tax rates")
st.divider()

# ----------------------------------------------------
# INPUT
# ----------------------------------------------------
salary_input = st.text_input(
    "Enter your annual income",
    placeholder="e.g. 1,000,000"
)

st.divider()

# ----------------------------------------------------
# TABS (Mobile UX)
# ----------------------------------------------------
monthly_tab, annual_tab = st.tabs(["Monthly Breakdown", "Annual Breakdown"])

# ----------------------------------------------------
# MONTHLY TAB (PLACEHOLDERS ONLY)
# ----------------------------------------------------
with monthly_tab:
    m_income = st.empty()
    m_tax = st.empty()
    m_net = st.empty()

    m_income.metric("Monthly Income", "₦0.00")
    m_tax.metric("Monthly Tax", "₦0.00")
    m_net.metric("Monthly Net Income", "₦0.00")

# ----------------------------------------------------
# ANNUAL TAB (PLACEHOLDERS ONLY)
# ----------------------------------------------------
with annual_tab:
    a_income = st.empty()
    a_tax = st.empty()
    a_net = st.empty()

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

            # --- Annual ---
            annual_tax = calculate_paye(salary)
            annual_net = salary - annual_tax

            # --- Monthly ---
            monthly_salary = salary / 12
            monthly_tax = annual_tax / 12
            monthly_net = monthly_salary - monthly_tax

            # --- Update Monthly ---
            m_income.metric("Monthly Income", f"₦{monthly_salary:,.2f}")
            m_tax.metric("Monthly Tax", f"₦{monthly_tax:,.2f}")
            m_net.metric("Monthly Net Income", f"₦{monthly_net:,.2f}")

            # --- Update Annual ---
            a_income.metric("Annual Income", f"₦{salary:,.2f}")
            a_tax.metric("Annual Tax", f"₦{annual_tax:,.2f}")
            a_net.metric("Annual Net Income", f"₦{annual_net:,.2f}")

            st.success("Calculation complete")

        except ValueError:
            st.error("Enter a valid amount (e.g. 1,000,000)")