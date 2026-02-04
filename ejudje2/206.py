n = int(input())
numbers = list(map(int, input().split()))
max = -10000000
for num in numbers:
    if num > max:
        max = num
print(max)