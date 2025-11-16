import cProfile
from multiprocessing import Pool
# from functools import cache

# @cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# multiprocessing == 12 secs
def main():
    inputs = [35, 36, 37, 38]
    # outputs = [fib(number) for number in inputs]
    with Pool() as pool:
        outputs = pool.map(fib, inputs)

# # cache method == 0 secs
# def main():
#     inputs = [35, 36, 37, 38]
#     for input in inputs:
#         fib(input)

if __name__ == '__main__':
    cProfile.run("main()", sort="cumtime")
