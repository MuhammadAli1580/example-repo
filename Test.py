import json
import random
import os

USERS_FILE = "users.json"

# 🔐 Load users from file or create an empty dict
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=4)

# 🔐 Sign up or log in users
def login():
    users = load_users()

    # Pre-fill the test user if no users exist
    if not users:
        print("⚠️ No Users Found. Creating A Test User (admin:1234) Automatically.")
        users['admin'] = {"password": "1234"}
        save_users(users)

    print("🔐 Welcome To Finance Toolkit Login")
    while True:
        action = input("🆕 New User? Type 'Signup' Or 'Login': ").lower()
        if action == 'signup':
            username = input("👤 Choose A Username: ")
            if username in users:
                print("⚠️ Username Already Exists.")
                continue
            password = input("🔑 Set Your Password: ")
            users[username] = {"password": password}
            save_users(users)
            print("✅ Signup Successful! You Can Now Login.\n")
        elif action == 'login':
            username = input("👤 Username: ")
            password = input("🔑 Password: ")
            if username in users and users[username]["password"] == password:
                print(f"✅ Welcome Back, {username}!\n")
                return username
            else:
                print("❌ Incorrect Credentials.")
        else:
            print("⚠️ Invalid Choice. Type 'Signup' Or 'Login'.")

# 🔢 Math practice
def basic_math():
    print("\n🔢 Let's Do Some Quick Math!")
    num1 = int(input("🔹 Enter Your First Number: "))
    num2 = int(input("🔹 Enter Your Second Number: "))
    print("1️⃣Add\n2️⃣Subtract\n3️⃣Multiply\n4️⃣Divide")
    operator = int(input("🔧 Choose An Operation: "))

    if operator == 1:
        result = num1 + num2
    elif operator == 2:
        result = num1 - num2
    elif operator == 3:
        result = num1 * num2
    elif operator == 4:
        result = num1 / num2 if num2 != 0 else "⚠️ Can't Divide By Zero!"
    else:
        result = "❌ Invalid Operator"

    print(f"✅ Result: {num1} {operator} {num2} = {result}")

# 💡 Budget tips
def smart_budget_tip(income, expenses):
    savings = income - expenses
    savings_percent = (savings / income) * 100 if income > 0 else 0

    print("\n💡 Smart Budget Tip:")
    if savings_percent >= 20:
        print("🎯 You're Saving Well! Try Investing Some Of It.")
    elif 0 < savings_percent < 20:
        print("📈 Try To Push Your Savings To At Least 20%!")
    elif savings_percent == 0:
        print("😬 You're Spending Every Rand. Consider Cutting A Few Expenses.")
    else:
        print("🚨 You're Overspending! Time To Tighten The Budget.")

# 🚨 Spending alert system
def spending_alerts(expenses, income):
    print("\n🚨 Spending Alerts:")
    for category, amount in expenses.items():
        if amount > 0.5 * income:
            print(f"⚠️ You Spent R{amount:.2f} On '{category}', Which Is Over 50% Of Your Income!")

# 💰 Budget calculator
def budget_calculator(income):
    print("\n💰 Time To Plan Your Monthly Budget!")
    expenses = {}
    while True:
        category = input("📂 Enter Any Expense Category (type 'done' to finish): ")
        if category.lower() == 'done':
            break
        amount = float(input(f"💸 How Much For '{category}'? R"))
        expenses[category] = expenses.get(category, 0) + amount

    total_expenses = sum(expenses.values())
    savings = income - total_expenses

    print("\n📊 --- Budget Summary ---")
    for cat, amt in expenses.items():
        print(f"🧾 {cat}: R{amt:.2f}")
    print(f"\n💸 Total Expenses: R{total_expenses:.2f}")
    print(f"💚 Remaining Savings: R{savings:.2f}")

    spending_alerts(expenses, income)
    smart_budget_tip(income, total_expenses)

# 📈 Compound Interest
def compound_interest():
    print("\n📈 Let's Calculate Compound Interest!")
    P = float(input("💰 Enter The Principal Amount: R"))
    r = float(input("📉 Enter The Annual Interest Rate (in %): ")) / 100
    t = float(input("🕐 Enter Time In Years: "))
    n = int(input("🔁 How Many Times Per Year Is It Compounded? "))
    A = P * (1 + r/n) ** (n*t)
    print(f"\n💹 Your Investment Will Grow To: R{A:.2f} 📈")

# 🧾 Loan calculator
def loan_calculator():
    print("\n🏦 Loan Repayment Calculator")
    loan = float(input("💳 Enter Loan Amount: R"))
    annual_rate = float(input("📊 Enter Annual Interest Rate (%): ")) / 100
    years = int(input("📅 Loan Term In Years: "))
    months = years * 12
    monthly_rate = annual_rate / 12

    if monthly_rate == 0:
        emi = loan / months
    else:
        emi = loan * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

    total_payment = emi * months
    interest_paid = total_payment - loan

    print(f"\n💵 Monthly Payment (EMI): R{emi:.2f}")
    print(f"📆 Total Payment: R{total_payment:.2f}")
    print(f"🧮 Total Interest Paid: R{interest_paid:.2f}")

# 📝 Expense Tracker
def expense_tracker():
    print("\n📝 Expense Tracker")
    expenses = {}
    while True:
        category = input("📂 Enter An Expense Category (or type 'done' to finish): ").lower()
        if category.lower() == 'done':
            break
        amount = float(input(f"💸 How Much For '{category}'? R"))
        expenses[category] = expenses.get(category, 0) + amount

    print("\n📊 --- Expense Summary ---")
    for cat, amt in expenses.items():
        print(f"🧾 {cat}: R{amt:.2f}")

# 💰 Savings Goal Tracker
def savings_goal():
    print("\n💰 Set Your Savings Goal")
    goal_amount = float(input("🎯 What Is Your Savings Goal? R"))
    current_savings = float(input("💸 How Much Have You Saved So Far? R"))
    remaining = goal_amount - current_savings

    if remaining <= 0:
        print("🎉 Congratulations! You've Reached Your Savings Goal!")
    else:
        print(f"💪 Keep Going! You Need R{remaining:.2f} More To Reach Your Goal.")

# 📈 Investment Tracker
def investment_tracker():
    print("\n📈 Track Your Investment Portfolio")
    investments = {}

    while True:
        name = input("📂 Enter Any Investment Name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break

        invested = float(input(f"💸 How Much Did You Invest In '{name}'? R"))
        current_value = float(input(f"📈 What’s The Current Value Of Your '{name}' Investment? R"))

        # Store only if not 'done'
        investments[name] = {
            'invested': invested,
            'current_value': current_value
        }

    print("\n📊 --- Investment Summary ---")
    for name, values in investments.items():
        profit_or_loss = values['current_value'] - values['invested']
        status = "📈 Profit" if profit_or_loss > 0 else "🔻 Loss" if profit_or_loss < 0 else "⚖️ No Gain"
        print(f"💼 {name}: Invested R{values['invested']:.2f}, Current R{values['current_value']:.2f} → {status} of R{profit_or_loss:.2f}")

# 📋 Menu
def show_menu():
    print("\n🌟 Finance Toolkit Menu")
    print("1️⃣ Basic Math Practice 🔢")
    print("2️⃣ Budget Calculator 💰 + Smart Tips 🧠")
    print("3️⃣ Compound Interest Calculator 📈")
    print("4️⃣ Loan Repayment Calculator 🧾")
    print("5️⃣ Expense Tracker 📝")
    print("6️⃣ Savings Goal Tracker 💰")
    print("7️⃣ Investment Tracker 📈")
    print("8️⃣ Exit ❌")

# 🏁 Main Program
user = login()
print(f"\n👋 Welcome, {user.capitalize()}! Let’s Master Your Money 💼💸")
income = float(input("💵 First Things First — What’s Your Monthly Income? R"))

while True:
    show_menu()
    choice = input("\n👉 Enter Your Choice (1-8): ")

    if choice == '1':
        basic_math()
    elif choice == '2':
        budget_calculator(income)
    elif choice == '3':
        compound_interest()
    elif choice == '4':
        loan_calculator()
    elif choice == '5':
        expense_tracker()
    elif choice == '6':
        savings_goal()
    elif choice == '7':
        investment_tracker()
    elif choice == '8':
        print(f"\n👋 Goodbye, {user}! Stay Sharp With Your Finances. See You Next Time 🫶")
        break
    else:
        print("❌ Invalid Input. Please Choose A Valid Option (1-8).")
