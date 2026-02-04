n = int(input())
numbers = list(map(int, input().split()))
c = 0
for num in numbers:
    if num > 0:
        c += 1
print(c)