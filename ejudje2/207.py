n = int(input())
numbers = list(map(int, input().split()))

max = -10000000
for num in numbers:
    if num > max:
        max = num

index = -1
for i in range(n):
    if numbers[i] == max:
        index = i + 1
        break

print(index)