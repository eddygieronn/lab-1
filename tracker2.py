# ==========================================
# Installment 3: The Tracker Does Math
# ==========================================

def main():
    # Banner
    print("==========================================")
    print("             EXPENSE TRACKER              ")
    print("          Know where your money goes.     ")
    print("==========================================")

    # Main Menu
    print("MAIN MENU")
    print("  [1] Add an expense         (coming soon)")
    print("  [2] View all expenses      (coming soon)")
    print("  [3] Show total spent       (coming soon)")
    print("  [4] Exit                   (coming soon)\n")

    # Name Prompt & Greeting
    name = input("What's your name? ")
    print(f"Welcome, {name}! Let's log two expenses.\n")

    # Questions / Inputs
    item1 = input("First expense? ")
    amount1 = float(input("Amount? "))

    item2 = input("Second expense? ")
    amount2 = float(input("Amount? "))

    tax_rate = float(input("Tax rate %? "))
    budget = float(input("Your budget? "))

    # Calculations
    subtotal = amount1 + amount2
    average = subtotal / 2
    tax = subtotal * (tax_rate / 100)
    grand_total = subtotal + tax
    over_budget = grand_total > budget
    left_in_budget = budget - grand_total

    # Summary
    print("\n----------------------------------------")
    print("SUMMARY")
    print(f"  - {item1 + ':':<10} ${amount1}")
    print(f"  - {item2 + ':':<10} ${amount2}")
    print(f"Subtotal:       ${subtotal}")
    print(f"Average:        ${average}")
    print(f"Tax ({tax_rate}%):     ${tax}")
    print(f"Grand total:    ${grand_total}")
    print(f"Over budget?    {over_budget}")
    print(f"Left in budget: ${left_in_budget}")
    print("----------------------------------------")

    # Footer
    print(f"Made by: {name}   |   Installment 3\n")

if __name__ == "__main__":
    main()