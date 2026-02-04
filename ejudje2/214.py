n = int(input())
arr = list(map(int, input().split()))

freq = [0] * 2001
for num in arr:
    freq[num + 1000] += 1

max_freq = max(freq)
answer = 1000

for i in range(2001):
    if freq[i] == max_freq:
        num = i - 1000
        if num < answer:
            answer = num

print(answer)