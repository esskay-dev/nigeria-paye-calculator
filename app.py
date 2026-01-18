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
# HIDE STREAMLIT DEFAULT UI
# ----------------------------------------------------
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ----------------------------------------------------
# HELPER FUNCTION (FORMAT NAIRA)
# ----------------------------------------------------
def format_naira(amount):
    return f"₦{amount:,.2f}"

# ----------------------------------------------------
# UI HEADER
# ----------------------------------------------------
st.title("Nigeria PAYE Tax Calculator")
st.write("Calculate your PAYE tax based on Nigeria's new tax rates.")

salary_input = st.text_input(
    "Enter your annual income",
    placeholder="e.g. 1,00,000"
)

st.divider()

# ----------------------------------------------------
# MONTHLY BREAKDOWN PLACEHOLDERS
# ----------------------------------------------------
st.subheader("Monthly Breakdown")

m_col1, m_col2, m_col3 = st.columns(3)

m_income = m_col1.empty()
m_tax = m_col2.empty()
m_net = m_col3.empty()

m_income.metric("Monthly Income", "₦0.00")
m_tax.metric("Monthly Tax", "₦0.00")
m_net.metric("Monthly Net Income", "₦0.00")

# ----------------------------------------------------
# ANNUAL BREAKDOWN PLACEHOLDERS
# ----------------------------------------------------
st.subheader("Annual Breakdown")

a_col1, a_col2, a_col3 = st.columns(3)

a_income = a_col1.empty()
a_tax = a_col2.empty()
a_net = a_col3.empty()

a_income.metric("Annual Income", "₦0.00")
a_tax.metric("Annual Tax", "₦0.00")
a_net.metric("Annual Net Income", "₦0.00")

st.divider()

# ----------------------------------------------------
# CALCULATE BUTTON
# ----------------------------------------------------
if st.button("Calculate Tax"):
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

            st.success("Calculation Complete")

            # Update Monthly Metrics
            m_income.metric("Monthly Income", format_naira(monthly_salary))
            m_tax.metric("Monthly Tax", format_naira(monthly_tax))
            m_net.metric("Monthly Net Income", format_naira(monthly_net))

            # Update Annual Metrics
            a_income.metric("Annual Income", format_naira(salary))
            a_tax.metric("Annual Tax", format_naira(annual_tax))
            a_net.metric("Annual Net Income", format_naira(annual_net))

        except ValueError:
            st.error("Please enter a valid amount (e.g. 1,000,000)")