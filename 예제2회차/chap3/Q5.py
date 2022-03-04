from itertools import combinations
n, m = map(int, input().split())
weight = list(map(int, input().split()))

# N개의 볼링공이 있을 때 2개 고르는 combination 구하기
comb = list(combinations(range(len(weight)), 2))

# 두 볼링공이 무개가 다른 경우만count
count = 0
for c in comb:
    if weight[c[0]] != weight[c[1]]:
        count += 1

print(count)