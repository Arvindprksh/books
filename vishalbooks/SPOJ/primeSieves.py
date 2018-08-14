from math import sqrt
import timeit


def algo_optimized(a):
    listofNumbers = list(range(a[0], a[1]))
    for i in range(2, int(sqrt(max(a)))):
        for j in listofNumbers:
            if j % i == 0:
                try:
                    listofNumbers.remove(j)
                except:
                    continue
    return listofNumbers


def naive_algo(a):
    primes = []
    for num in range(a[0], a[1] + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


if __name__ == "__main__":
    n = int(input())
    numbers, primes = [], []
    for i in range(n):
        numbers.append([int(x) for x in input().split()])

        start_time_1 = timeit.default_timer()
        primes.append(naive_algo(numbers[i]))
        elapsed_1 = timeit.default_timer() - start_time_1
        print("Naive Algorithm ETA : {}".format(elapsed_1))

        start_time = timeit.default_timer()
        primes.append(algo_optimized(numbers[i]))
        elapsed = timeit.default_timer() - start_time
        print("Optimized algorithm ETA : {}".format(elapsed))

        for i in range(len(primes)):
            for j in range(len(primes[i])):
                print(primes[i][j])
        print('\n')
