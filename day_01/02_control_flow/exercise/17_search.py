items = ["rice", "noodles", "toyo", "spam", "coffee"]
item_to_find = "spam"

# for item in items:
#     # TODO: If item equals the item_to_find
#     #  # print and exit loop
#     pass


################################################## answer
item_found = False
for item in items:
    # print(".")
    if item == item_to_find:
        print(item)
        item_found = True
        break
print("Item found:", item_found)