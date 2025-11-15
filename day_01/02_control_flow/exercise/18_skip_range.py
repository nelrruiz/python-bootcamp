for item in range(100):
    # TODO: Change code to skip printing numbers 20, 21, ..., 79, 80.
    print(item)


############################# answer
for number in range(1,100+1):
    #skip 21-79
    if 21 <= number <= 79:
        continue
    print(number)

