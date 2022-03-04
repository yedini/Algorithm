from itertools import combinations
n, m = map(int, input().split())
weight = list(map(int, input().split()))

comb = list(combinations(range(len(weight)), 2))

count = 0
for c in comb:
    if weight[c[0]] != weight[c[1]]:
        count += 1

print(count)