n = int(input())
numbers = list(map(int, input().split()))

max = -10000000
min = 10000000
for num in numbers:
    if num > max:
        max = num
    if num < min:
        min = num


for i in range(n):
    if numbers[i] == max:
        numbers[i] = min

for i in range(n):
    print(numbers[i], end=' ')
