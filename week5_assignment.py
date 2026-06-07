# Week 5 Assignment
# Arvin Tandukar

# Q1 - Bank account manager

print("===== Question 1 =====")


class BankAccount:

    def __init__(self, name, account_number, balance=0):

        self.name = name
        self.account_number = account_number
        self.balance = balance

    # add money
    def deposit(self, amount):

        self.balance += amount

    # withdraw money
    def withdraw(self, amount):

        if amount > self.balance:
            print(f"{self.name}: Insufficient funds")

        else:
            self.balance -= amount

    # show balance
    def get_balance(self):

        print(f"{self.name} ({self.account_number}) - NPR {self.balance}")


account1 = BankAccount("Ramesh Thapa", "A001", 5000)
account2 = BankAccount("Sunita Karki", "A002", 0)
account3 = BankAccount("Bikash Rai", "A003", 12000)

account2.deposit(3000)
account3.withdraw(15000)
account1.withdraw(2000)

print("\nFinal Balances:")

account1.get_balance()
account2.get_balance()
account3.get_balance()


# Q2 - Student report card

print("\n===== Question 2 =====")


class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    # calculate average
    def average(self):

        return sum(self.marks) / len(self.marks)

    # determine grade
    def grade(self):

        avg = self.average()

        if avg >= 80:
            return "A"

        elif avg >= 65:
            return "B"

        elif avg >= 50:
            return "C"

        elif avg >= 40:
            return "D"

        else:
            return "F"

    # display result
    def display(self):

        avg = self.average()

        status = "Pass" if avg >= 40 else "Fail"

        print(
            f"{self.name} | Average: {avg:.2f} | "
            f"Grade: {self.grade()} | {status}"
        )


students = [
    ("Aarav", [78, 85, 60, 90, 72]),
    ("Sita", [45, 50, 38, 60, 55]),
    ("Bishal", [30, 25, 40, 35, 28]),
    ("Priya", [90, 88, 95, 92, 87]),
]

# create objects and display results
for name, marks in students:

    student = Student(name, marks)

    student.display()


    # Q3 - Food delivery app

print("\n===== Question 3 =====")


class DeliveryPartner:

    def __init__(self, name, partner_id, deliveries):

        self.name = name
        self.partner_id = partner_id
        self.deliveries = deliveries

    # will be overridden
    def total_earning(self):

        return 0

    # display partner details
    def display(self):

        print(
            f"{self.name} | Deliveries: {self.deliveries} | "
            f"Earning: NPR {self.total_earning()}"
        )


class BikeRider(DeliveryPartner):

    def __init__(self, name, partner_id, deliveries, km_travelled):

        super().__init__(name, partner_id, deliveries)

        self.km_travelled = km_travelled

    def total_earning(self):

        return (self.deliveries * 80) + (self.km_travelled * 5)


class Walker(DeliveryPartner):

    def __init__(self, name, partner_id, deliveries, rainy_deliveries):

        super().__init__(name, partner_id, deliveries)

        self.rainy_deliveries = rainy_deliveries

    def total_earning(self):

        return (self.deliveries * 60) + (self.rainy_deliveries * 50)


class CarDriver(DeliveryPartner):

    def __init__(self, name, partner_id, deliveries, fuel_cost):

        super().__init__(name, partner_id, deliveries)

        self.fuel_cost = fuel_cost

    def total_earning(self):

        return (self.deliveries * 120) - self.fuel_cost


partners = [
    BikeRider("Santosh Rai", "B-01", 15, 42),
    Walker("Kabita Maharjan", "W-01", 18, 5),
    CarDriver("Roshan KC", "C-01", 20, 850),
]

# show all partners
for partner in partners:

    partner.display()

# find highest earning partner
highest = partners[0]

for partner in partners:

    if partner.total_earning() > highest.total_earning():

        highest = partner

print(
    f"\nHighest Earner: {highest.name} "
    f"(NPR {highest.total_earning()})"
)


# Q4 - Bus ticket booking

print("\n===== Question 4 =====")


class Bus:

    def __init__(self, route, total_seats):

        self.route = route
        self.total_seats = total_seats
        self.booked = {}

    # book a seat
    def book_seat(self, seat_number, passenger_name):

        if seat_number in self.booked:

            print(f"Seat {seat_number} already booked")

        else:

            self.booked[seat_number] = passenger_name

            print(f"Seat {seat_number} booked for {passenger_name}")

    # count remaining seats
    def available_seats(self):

        return self.total_seats - len(self.booked)

    # show passenger list
    def passenger_list(self):

        print("\nPassenger List:")

        for seat, passenger in sorted(self.booked.items()):

            print(f"Seat {seat}: {passenger}")


bus = Bus("Kathmandu - Pokhara", 10)

bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),
    (1, "Prakash Magar"),
    (7, "Suman Tamang"),
]

# process bookings
for seat, passenger in bookings:

    bus.book_seat(seat, passenger)

print(f"\nAvailable Seats: {bus.available_seats()}")

bus.passenger_list()