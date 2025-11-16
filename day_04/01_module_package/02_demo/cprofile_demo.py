import cProfile #to test if a code is fast or slow; dependent on your laptop's RAM, CPU usage, and computing powers


def main():
    for _ in range(1_000_000):
        x = 10 ** 1000


if __name__ == '__main__':
    cProfile.run("main()") 
