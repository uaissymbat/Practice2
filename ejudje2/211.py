n, l, r = map(int, input().split())
arr = list(map(int, input().split()))

l0 = l - 1
r0 = r - 1

arr[l0:r0+1] = arr[l0:r0+1][::-1]

for num in arr:
    print(num, end=' ')