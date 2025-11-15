# Ask the cost and pax or count for three separate items
item_cost_1 = None  # Let the user enter a number
item_count_1 = None  # Let the user enter a number

item_cost_2 = None  # Let the user enter a number
item_count_2 = None  # Let the user enter a number

item_cost_3 = None  # Let the user enter a number
item_count_3 = None  # Let the user enter a number

# Calculate the total
total = None
print(total)

########################## answers

# Ask the cost and pax or count for three separate items
item_cost_1 = int(input("Enter the cost for item 1:"))
item_count_1 = int(input("Enter the count for item 1:"))

item_cost_2 = int(input("Enter the cost for item 2:"))
item_count_2 = int(input("Enter the count for item 2:"))

item_cost_3 = int(input("Enter the cost for item 3:"))
item_count_3 = int(input("Enter the count for item 3:"))

# Calculate the total
total_cost = item_cost_1 + item_cost_2 + item_cost_3
total_count = item_count_1 + item_count_2 + item_count_3
print("Total cost:", total_cost)
print("Total count:", total_count)

total = (item_cost_1*item_count_1)+(item_cost_2*item_count_2)+(item_cost_3*item_count_3)
print("Breakdown of costs:", f"({item_count_1}*{item_cost_1})+({item_count_2}*{item_cost_2})+({item_count_3}*{item_cost_3})={total}")
print("Overall Total:", total)
