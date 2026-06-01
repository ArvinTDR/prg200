# Question 1 — ATM Withdrawal Validator
print("===== Question 1 =====")

balance = float(input("Enter current balance: "))
daily_withdrawn = float(input("Enter amount already withdrawn today: "))
amount = float(input("Enter withdrawal amount: "))

daily_limit = 50000

if amount % 500 != 0:
    print("Invalid amount. Must be a multiple of NPR 500.")

elif amount > balance:
    print("Insufficient balance.")

elif daily_withdrawn + amount > daily_limit:
    print("Daily withdrawal limit reached.")

else:
    balance -= amount
    print("Withdrawal successful.")
    print(f"Your current balance after withdrawal: NPR {balance}")


# Question 2 — Online Store Discount System

print("\n===== Question 2 =====")

purchase = float(input("Enter total purchase amount: "))

member = input("Are you a loyalty member? (yes/no): ").lower()

discount = 0

if purchase < 1000:
    discount = 0

elif purchase <= 4999:
    discount = 0.05

elif purchase <= 14999:
    discount = 0.10

else:
    discount = 0.20

discounted_amount = purchase - (purchase * discount)

# Extra 5% for loyalty members
if member == "yes":
    discounted_amount -= discounted_amount * 0.05

print(f"Final payable amount: NPR {discounted_amount:.2f}")


# Question 3 — Inventory Restock Alert

print("\n===== Question 3 =====")

inventory = [
    {"item": "Rice", "stock": 5, "threshold": 10},
    {"item": "Eggs", "stock": 24, "threshold": 12},
    {"item": "Milk", "stock": 3, "threshold": 6},
    {"item": "Bread", "stock": 8, "threshold": 5},
    {"item": "Chicken", "stock": 0, "threshold": 4},
    {"item": "Cooking Oil", "stock": 2, "threshold": 3},
]

restock_count = 0

for product in inventory:

    if product["stock"] < product["threshold"]:

        print(f"Restock Alert: {product['item']}")

        restock_count += 1

print(f"Total items needing restock: {restock_count}")


# Question 4 — Password Strength Checker

print("\n===== Question 4 =====")

passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

special_characters = "!@#$%^&*"

for password in passwords:

    print(f"\nChecking password: {password}")

    missing = []

    # Length check
    if len(password) < 8:
        missing.append("At least 8 characters")

    # Uppercase check
    if not any(char.isupper() for char in password):
        missing.append("One uppercase letter")

    # Lowercase check
    if not any(char.islower() for char in password):
        missing.append("One lowercase letter")

    # Digit check
    if not any(char.isdigit() for char in password):
        missing.append("One digit")

    # Special character check
    if not any(char in special_characters for char in password):
        missing.append("One special character")

    if len(missing) == 0:
        print("Strong password")

    else:
        print("Weak password")
        print("Missing criteria:")

        for item in missing:
            print("-", item)


# Question 5 — Taxi Fare Calculator

print("\n===== Question 5 =====")

trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

for trip in trips:

    distance = trip["distance"]
    hour = trip["hour"]

    fare = 0

    # Base fare
    if distance <= 2:
        fare = 150

    # 3km to 10km
    elif distance <= 10:
        extra_km = distance - 2
        fare = 150 + (extra_km * 35)

    # Beyond 10km
    else:
        first_section = 8 * 35
        remaining = distance - 10

        fare = 150 + first_section + (remaining * 28)

    # Night surcharge
    if hour >= 22 or hour < 5:
        fare += fare * 0.10

    print(f"\nDistance: {distance} km")
    print(f"Hour: {hour}")
    print(f"Taxi Fare: NPR {fare:.2f}")

    