# Week 4 Assignment
# Arvin Tandukar

# Q1 - Grocery billing system

inventory = {
    "rice": {"price": 120, "stock": 20},
    "milk": {"price": 90, "stock": 10},
    "bread": {"price": 60, "stock": 15},
    "eggs": {"price": 15, "stock": 30}
}

cart = {
    "rice": 2,
    "milk": 3,
    "eggs": 12
}


def process_order(inventory, cart):

    total = 0

    print("---- Bill ----")

    for item, qty in cart.items():

        # stock available
        if item in inventory and inventory[item]["stock"] >= qty:

            cost = inventory[item]["price"] * qty
            total += cost

            inventory[item]["stock"] -= qty

            print(f"{item} x{qty} = NPR {cost}")

        else:
            print(f"Sorry, not enough stock for {item}")

    print(f"Grand Total: NPR {total}")

    # remaining stock
    print("\nUpdated stock:")

    for item in inventory:
        print(f"{item} = {inventory[item]['stock']}")


process_order(inventory, cart)


# Q2 - Water level checker

print("\n===== Question 2 =====")

sensors = [
    ("Chatara", 2.8),
    ("Tribeni Ghat", 5.4),
    ("Koshi Barrage", 4.1),
    ("Sunsari Bridge", 1.9),
    ("Saptakoshi Camp", 6.0),
]


def check_water_level(location, level_metres):

    if level_metres < 3:
        return "Safe"

    elif level_metres <= 5:
        return "Warning — Alert nearby villages"

    else:
        return "DANGER — Evacuate immediately!"


for location, level in sensors:

    result = check_water_level(location, level)

    print(f"{location} ({level} m): {result}")


# Q3 - Date converter
print("\n===== Question 3 =====")

bs_months = [
    "Baisakh", "Jestha", "Ashadh", "Shrawan",
    "Bhadra", "Ashwin", "Kartik", "Mangsir",
    "Poush", "Magh", "Falgun", "Chaitra"
]

customers = [
    {"name": "Ramesh Thapa", "date": "1985-06-24", "cal": "AD", "need": "BS", "style": "full"},
    {"name": "Sunita Karki", "date": "2055-09-10", "cal": "BS", "need": "AD", "style": "iso"},
    {"name": "Bikash Rai", "date": "1998-11-30", "cal": "AD", "need": "BS", "style": "nepali"},
    {"name": "Anjali Gurung", "date": "2040-01-05", "cal": "BS", "need": "AD", "style": "full"}
]


def convert_date(date_str, from_cal, to_cal):

    year, month, day = map(int, date_str.split("-"))

    # same calendar, no conversion needed
    if from_cal == to_cal:
        return date_str

    # AD to BS conversion
    if from_cal == "AD" and to_cal == "BS":

        new_year = year + 56
        month_name = bs_months[(month - 1) % 12]

        return f"{day}th {month_name}, {new_year} BS"

    # BS to AD conversion
    elif from_cal == "BS" and to_cal == "AD":

        new_year = year - 56

        return f"{new_year}-{month:02d}-{day:02d} AD"


# display customer records
for customer in customers:

    converted = convert_date(
        customer["date"],
        customer["cal"],
        customer["need"]
    )

    print(
        f"{customer['name']} | "
        f"Original: {customer['date']} {customer['cal']} | "
        f"Converted: {converted}"
    )


    # Q4 - Word frequency counter

print("\n===== Question 4 =====")

text = """
Nepal is a beautiful country. Nepal has Mount Everest.
Everest is the highest mountain in the world. Many tourists
visit Nepal every year to see Everest and other mountains.
Nepal is known for its mountains and natural beauty.
"""


def word_frequency(text):

    # remove punctuation
    text = text.replace(".", "").replace(",", "")

    # convert to lowercase
    words = text.lower().split()

    counts = {}

    # count each word
    for word in words:

        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    # sort by frequency
    sorted_words = sorted(
        counts.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_words[:3]


top_words = word_frequency(text)

print("Top 3 words:")

for word, count in top_words:
    print(f"{word} — {count} times")


    # Q5 - ATM simulator

print("\n===== Question 5 =====")

accounts = {
    "A001": {"name": "Ramesh Thapa", "balance": 15000, "pin": "1234"},
    "A002": {"name": "Sunita Karki", "balance": 8500, "pin": "5678"},
    "A003": {"name": "Bikash Rai", "balance": 22000, "pin": "9012"}
}


def atm(account_id, pin, action, amount=0):

    # account check
    if account_id not in accounts:
        print("Account not found")
        return

    account = accounts[account_id]

    # pin verification
    if account["pin"] != pin:
        print("Incorrect PIN")
        return

    # balance inquiry
    if action == "balance":

        print(f"Name: {account['name']}")
        print(f"Balance: NPR {account['balance']}")

    # deposit money
    elif action == "deposit":

        account["balance"] += amount

        print(f"Deposited NPR {amount}")
        print(f"New Balance: NPR {account['balance']}")

    # withdraw money
    elif action == "withdraw":

        if amount > account["balance"]:
            print("Insufficient funds")

        else:
            account["balance"] -= amount

            print(f"Withdrawn NPR {amount}")
            print(f"Remaining Balance: NPR {account['balance']}")


atm("A001", "1234", "balance")
print()

atm("A002", "0000", "withdraw", 2000)
print()

atm("A002", "5678", "deposit", 3000)
print()

atm("A003", "9012", "withdraw", 25000)
print()

atm("A004", "1111", "balance")