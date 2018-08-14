#python3
n = int(input())
numbers = [int(x) for x in input().split()]
len_num = len(numbers)
assert(len_num == n)
max_num_index = -1
second_max_num_index = -1

for i in range(len_num):
    if max_num_index is -1 or numbers[i] > numbers[max_num_index]:
        second_max_num_index = max_num_index
        max_num_index = i 

    if numbers[i] > numbers[second_max_num_index] and i is not max_num_index:
        second_max_num_index = i

print(numbers[second_max_num_index] * numbers[max_num_index])






