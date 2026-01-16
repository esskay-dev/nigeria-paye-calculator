# ----------------------------------------------------
# USER INPUT
# ----------------------------------------------------

def get_annual_income():
    '''Prompts user for annual income and 
    validates inputs.'''
    while True:
        user_input = input("Enter your annual income:")

        if user_input.strip() == "":
            print("Please enter your annual income.")
            continue
        try:
            return float(user_input.replace(",", ""))
        except ValueError:
            print("Enter amount only (e.g. 1,000,000)")

# ----------------------------------------------------
# PAYE TAX CALCULATION
# ----------------------------------------------------

def calculate_paye(salary):
    '''Calculates PAYE tax based on Nigeria new tax rates'''
    remaining_income = salary
    tax = 0.0

    # Band 1: First N800,000 at 0%
    band = min(remaining_income, 800_000)
    tax += band * 0.0
    remaining_income -= band

    # Band 2: Next N2,200,000 at 15%
    if remaining_income > 0:
        band = min(remaining_income, 2_200_000)
        tax += band * 0.15
        remaining_income -= band

    # Band 3: Next N9,000,000 at 18%
    if remaining_income > 0:
        band = min(remaining_income, 9_000_000)
        tax += band * 0.18
        remaining_income -= band

    # Band 4: Next N13,000,000 at 21%
    if remaining_income > 0:
        band = min(remaining_income, 13_000_000)
        tax += band * 0.21
        remaining_income -= band

    # Band 5: Above N67,849,999 at 23%
    if remaining_income > 0:
        band = min(remaining_income, 25_000_000)
        tax += band * 0.23
        remaining_income -= band

    # Band 6: Above N50,000, 000 at 25%
    if remaining_income > 0:
        tax += remaining_income * 0.25

    return tax

# ----------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------

def main():
    print("=" * 40)
    print("NIGERIA PAYE TAX CALCULATOR")
    print("=" * 40)

    salary = get_annual_income()
    total_tax = calculate_paye(salary)
    net_salary = salary - total_tax

    print("\n--- PAYE TAX SUMMARY ...")
    print(f"Gross Salary: ₦{salary:,.2f}")
    print(f"Total Tax: ₦{total_tax:,.2f}")
    print(f"Net Salary: ₦{net_salary:,.2f}")

    input("\nPress Enter to exit...")

# ----------------------------------------------------
# SCRIPT ENTRY POINT
# ----------------------------------------------------

if __name__ == "__main__":
    main()