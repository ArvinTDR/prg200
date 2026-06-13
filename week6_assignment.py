# Week 6 Assignment
# Arvin Tandukar

# Q1 - Temperature logger

import math

station_name = "Kathmandu Weather Station"

temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]

# calculate average
def get_average(temps):

    return sum(temps) / len(temps)

# calculate standard deviation
def get_deviation(temps):

    mean = get_average(temps)   # local variable

    variance = 0

    for temp in temps:

        variance += (temp - mean) ** 2

    variance = variance / len(temps)

    return math.sqrt(variance)

# display summary
def get_summary(temps):

    print("===== Question 1 =====")
    print(station_name)

    print(f"Minimum Temperature: {min(temps)}")
    print(f"Maximum Temperature: {max(temps)}")
    print(f"Average Temperature: {get_average(temps):.2f}")
    print(f"Standard Deviation: {get_deviation(temps):.2f}")


get_summary(temperatures)

# print(mean)
# NameError because mean is a local variable inside get_deviation()


# Q2 - Bill splitter

import random

random.seed(42)

friends = ["Ramesh", "Sunita", "Bikash", "Anjali", "Dipak"]

total_bill = 3750

# split bill equally
def split_bill(friends, total):

    return total / len(friends)

# pick random friend
def pick_lucky(friends):

    return random.choice(friends)

# display final bill summary
def final_summary(friends, total):

    print("\n===== Question 2 =====")

    share = split_bill(friends, total)

    lucky_person = pick_lucky(friends)

    for friend in friends:

        print(f"{friend}: NPR {share:.2f}")

    lucky_total = share + 50  # local variable

    print(f"\nLucky Person: {lucky_person}")
    print(f"{lucky_person} pays NPR {lucky_total:.2f}")


final_summary(friends, total_bill)


# Q3 - Exam scheduler

import datetime

college_name = "Bhaktapur Multiple Campus"

start_date = "2025-05-01"

exams = [
    ("Python Programming", 0),
    ("Data Structures", 3),
    ("Database Systems", 6),
    ("Computer Networks", 10),
    ("Mathematics", 14),
]

# convert string to datetime
def parse_date(date_str):

    return datetime.datetime.strptime(date_str, "%Y-%m-%d")

# calculate exam date
def get_exam_date(start_str, days):

    start = parse_date(start_str)

    exam_date = start + datetime.timedelta(days=days)

    return exam_date.strftime("%Y-%m-%d")

# display exam schedule
def print_schedule(start_str, exams):

    print("\n===== Question 3 =====")
    print(college_name)

    for subject, days in exams:

        print(f"{subject}: {get_exam_date(start_str, days)}")


print_schedule(start_date, exams)


# Q4 - Shopping discount

from discount import final_price, TAX_RATE

products = [
    ("Laptop", 85000, 10),
    ("Headphones", 4500, 15),
    ("Phone Case", 800, 5),
    ("USB Cable", 600, 0),
]

print("\n===== Question 4 =====")
print(f"TAX_RATE = {TAX_RATE}")

# calculate final prices
for name, price, discount in products:

    final = final_price(price, discount)

    print(
        f"{name} | Original: NPR {price} | "
        f"Final: NPR {final:.2f}"
    )