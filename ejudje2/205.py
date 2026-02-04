n = int(input())
power_of_two = False

p = 1
while p <= n:
    if p == n:
        power_of_two = True
        break
    p *= 2

if power_of_two:
    print("YES")
else:
    print("NO")