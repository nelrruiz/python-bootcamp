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

# TODO: Remove the negative price in the list


######################################### answer

# TODO: Print the first, third, and last item
print("Current Price:", prices[0])
print("Current Price:", prices[2])
print("Current Price:", prices[-1])

# TODO: Change the first, third, and last values to half the price
indices = [0,2,-1]

for index in indices:
    prices[index] = int(prices[index]/2) #coule be prices[index]//=2

# TODO: Print the first, third, and last item again to see new price
print("New Price:", prices[0])
print("New Price:", prices[2])
print("New Price:", prices[-1])

# TODO: Remove the negative price in the list


for price in prices:
    if price < 0:
        index = prices.index(price)
        prices[index] = 0

print(prices)