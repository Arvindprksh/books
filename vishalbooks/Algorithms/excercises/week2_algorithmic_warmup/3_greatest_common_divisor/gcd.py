# Uses python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


if __name__ == "__main__":
    numbers = [int(x) for x in input().split()]
    print(numbers[0],numbers[1])
    print(gcd_naive(numbers[0], numbers[1]))
