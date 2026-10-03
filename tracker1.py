# ==========================================
# Installment 2: Talking to the User
# ==========================================

def main():
    # 1. Lab 1 Banner and Menu
    print("=" * 45)
    print("        EXPENSE TRACKER - MODULE 00")
    print("=" * 45)
    print("[1] Add an Expense")
    print("[2] View All Expenses")
    print("[3] View Expense Summary")
    print("[4] Exit")
    print("=" * 45)

    # 2 & 3. Personal greeting replacing the old welcome line
    name = input("Enter your name: ")
    print(f"Welcome, {name}! Let's log two expenses.\n")

    # 4 & 5. Ask for two expenses and store amounts as numbers
    item1 = input("First Expense?: ")
    amount1 = float(input(f"Amount? {item1}: "))

    item2 = input("Second Expense?: ")
    amount2 = float(input(f"Enter amount for {item2}: "))

    # Compute total and average
    total = amount1 + amount2
    average = total / 2

    # 6. SUMMARY between two - lines with values lined up
    print("\n" + "-" * 35)
    print("              SUMMARY              ")
    print("-" * 35)
    print(f"{item1:<20} {amount1:>12.2f}")
    print(f"{item2:<20} {amount2:>12.2f}")
    print("-" * 35)
    print(f"{'Total Spent:':<20} {total:>12.2f}")
    print(f"{'Average:':<20} {average:>12.2f}")
    print("-" * 35)

    # 7. Footer
    print(f"Made by: {name}  |  Installment 2\n")

if __name__ == "__main__":
    main()