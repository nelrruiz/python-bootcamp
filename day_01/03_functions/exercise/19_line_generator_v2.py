"""
    TODO: Create a function `line_generator` that has a parameter `number` and prints the following:
	Line 1
	Line 2
	...
	Line number
"""

# TODO: Use the function once
###################################################### answer


def line_generator(number):
	for item in range(1,int(number)+1):
		print("Line", item)

line_generator(7)