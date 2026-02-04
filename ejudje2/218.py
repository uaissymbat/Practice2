n = int(input())
first_occurrence = {}

for i in range(n):
    s = input().strip()
    if s not in first_occurrence:
        first_occurrence[s] = i + 1

sorted_strings = sorted(first_occurrence.keys())

for s in sorted_strings:
    print(s, first_occurrence[s])