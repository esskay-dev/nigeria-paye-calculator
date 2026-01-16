import streamlit as st
from tax import calculate_paye

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ----------------------------------------------------
# PAYE CALCULATION FUNCTION
# ----------------------------------------------------

def calculate_paye(salary):
    tax = 0
    remaining_income = salary

    bands = [
        (800_000,0.0),
        (2_200_000,0.15),
        (9_000_000,0.18),
        (13_000_000,0.21),
        (25_000_000,0.23),
    ]

    for limit, rate in bands:
        if remaining_income <= 0:
            break
        taxable = min(remaining_income, limit)
        tax += taxable * rate
        remaining_income -= taxable

    if remaining_income > 0:
        tax += remaining_income * 0.25
    
    return tax

# ----------------------------------------------------
# STREAMLIT UI
# ----------------------------------------------------
st.set_page_config(page_title="Nigeria PAYE Tax Calculator", layout="centered")

st.title("Nigeria PAYE Tax Calculator")
st.write("Calculate your PAYE tax based on Nigeria's new tax rates.")

salary_input = st.text_input("Enter your annual income", placeholder="e.g. 3,600,000")

if st.button("Calculate Tax"):
    if salary_input.strip() == "":
        st.error("Please enter your annual income.")
    else:
        try:
            salary = float(salary_input.replace(",", ""))
            tax = calculate_paye(salary)
            net = salary - tax

            st.success("Calculation Complete!")

            st.write(f"**Gross Salary:** ₦{salary:,.2f}")
            st.write(f"**Annual PAYE Tax:** ₦{tax:,.2f}")
            st.write(f"**Net Income:** ₦{net:,.2f}")

        except ValueError:
            st.error("Please enter your annual income (e.g. 3,600,000).")