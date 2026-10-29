# Lab 10: inventory.py

print("--- Exercise 1: Build the list ---")

inventory = ["pen","notebook","stapler","tape","marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index Practice ---")
print(inventory[0])
print(inventory[-1])
print(inventory[2])
middle = len(inventory) // 2
print(inventory[middle])

print("--- Exercise 3: Slicing Practice ---")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("--- Exercise 4: Modifying the list ---")
inventory.append("envelope")

print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("--- Exercise 5: Tuple comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coords, a location should never change by accident")

print(coords)

print("--- Exercise 6: Average List of sales ---")
sales = [100, 250, 75, 180, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total sales: {total}")
print(f"Count: {count}")
print(f"Average sales: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * .9, 2))

print("Original prices:", prices)
print("Discounted prices:", discount)

print("--- Exercise 8: Filter above a threshold ---")
sales = [340,127,589,204,467,88,731,315,62,490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")




# Reflection 1: What is the most surprising thing about how lists work in Python compared to what you expected coming in?

# The most surprising for me is how capitals and lowercase letters differ in priority, it's quite shocking that Z is before a.

# Reflection 2: Describe one real business situation — from a job you've had, an internship, or a class — where a Python list would have saved you time compared to doing it manually in Excel.

# A python list can save you time when you're evaluating the total, average, best, and worst sales figures, because you can iterate freely as well as using functions built in to evaluate the list properties quickly.