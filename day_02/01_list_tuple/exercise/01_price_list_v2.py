prices = [10_000, 20, 3_000, 3, -200, 1_000]

# TODO: Print the first, third, and last item
print("Current Price:")
print("Current Price:")
print("Current Price:")

# TODO: Change the first, third, and last values to half the price

# TODO: Print the first, third, and last item again to see new price
print("New Price:")
print("New Price:")
print("New Price:")

######################################### answer

# TODO: Print the first, third, and last item
print("Current Price:", prices[0])
print("Current Price:", prices[2])
print("Current Price:", prices[-1])

# prices[0] = prices[0]//2
# prices[2] = prices[2]//2
# prices[-1] = prices[-1]//2

# # TODO: Print the first, third, and last item again to see new price
# print("New Price:", prices[0])
# print("New Price:", prices[2])
# print("New Price:", prices[-1])


######################################### alternative answer

indices = [0,2,-1]

for index in indices:
    prices[index] = int(prices[index]/2)

# TODO: Print the first, third, and last item again to see new price
print("New Price:", prices[0])
print("New Price:", prices[2])
print("New Price:", prices[-1])