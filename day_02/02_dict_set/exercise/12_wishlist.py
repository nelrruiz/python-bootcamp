# TODO: Fill in the details of the item you plan to buy
order = {
    "Name": "Toblerone",
    "Info": "Dark Chocolate",
    "Price": 85,
    "Weight": "100g"
}

# TODO: Print the item details in the following format:
"""
Order:
	Name: item name
	Info: item info
	...
"""
############################################# answer

print("Order:")
for field, details in order.items():
    print(f"\t{field}: {details}")