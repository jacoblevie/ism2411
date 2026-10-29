#1. In Exercise 5 (Debug First, Then Ask), what was the first bug you spotted? Did you find it from the traceback, from a print() statement, from explaining the code out loud to the duck, or only after asking AI? What does that tell you about your current debugging instincts?

    # There was not a colon on the for loop on line 10. I found it from traceback. Then, I ran the code and got an error on line 16 so I checked that out. What I found was the code had a <= sign when it would only need a < sign since we are adding 1 to the index after printing it, so the loop will run once too many times since python starts counting at 0.

#2. Without looking at your code, explain in plain English what apply_discount(price, tier) does, what its inputs are, and what it returns. Could a colleague use it without reading the body?

    # apply_discount takes in a price and a tier. It checks the tier and applies a discount based on the tier. If the tier is gold, it applies a 15% discount, if silver, it applies a 10% discount, if bronze, it applies a 5% discount, and if none, it does not apply any discount. It returns the discounted price by multiplying the price by the discount percentage. A colleague could use it without reading the body as long as they know what the tiers are and what the discount percentages are.

#3. If you used AI on any part of today's lab, write the disclosure comment you would add to the top of your file. Then reflect: did the AI use build your understanding, or did it shortcut it?

    # I used AI suggestions on the auto fill, but that's built in to the software, can't help it. For Exercise 5, I was able to find both bugs before going to AI because it was relaitvely straightforward when it flagged the line that caused the error. 


# Exercise 1

#define calculate tax function

def calculate_tax(price,rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100,0.07)
tax2 = calculate_tax(250,0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
print(f"Another Tax: ${calculate_tax(150,0.05):.2f}")

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.9
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"Price for {tier} tier: ${apply_discount(price, tier):.2f}")

# Exercise 3

# wrie it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax 
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax
print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    final = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${final:.2f}")

# Exercise 6

x = 100 #apple, global

def double_it():
    #global x would call above apple, 100
    x = 999 #another apple (not same as above), local
    return x * 2

print(x)
print(double_it())
print(x)

# Exercise 5

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}")

count = 0
for sale in sales: #added a colon mark, syntax error
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): # changed <= to <, index out of range error because python starts counting at 0.
    print(sales[i])
    i += 1
