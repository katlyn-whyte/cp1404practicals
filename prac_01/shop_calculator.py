total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("price of the item: "))
    total += item_price

if total > 100:
    total *= 0.9
print(f"total price for {number_of_items} items is ${total:.2f}")

