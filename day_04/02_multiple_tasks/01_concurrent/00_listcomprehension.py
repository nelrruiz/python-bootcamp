costs = [10,20,30,40,50]

#new method
discounted_costs = [cost // 2 for cost in costs]

#another new 
def half_price(x):
    return x // 2
discounted_costs = [half_price(cost) for cost in costs] #add costs[::2] to get the half price for every 2 steps


print(discounted_costs)