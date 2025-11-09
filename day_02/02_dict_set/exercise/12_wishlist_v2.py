# TODO: Fill in the details of the items you plan to buy
wishlist = [
    {
    	"Name": "Toblerone",
    	"Info": "Dark Chocolate",
    	"Price": 85,
    	"Weight": "100g"
	},
    {
    	"Name": "Oreo",
    	"Info": "Double Stuff",
    	"Price": 50,
    	"Weight": "150g"
	},
    {
    	"Name": "Chips Ahoy",
    	"Info": "Original Chocolate Chip",
    	"Price": 25,
    	"Weight": "38g"
	}
]

# TODO: Print the item details in the following format (for each order):
"""
Order:
	Name: item name
	Info: item info
	...
"""
for order in wishlist:
	print("Order:")
	for field, details in order.items():
		print(f"\t{field}: {details}")