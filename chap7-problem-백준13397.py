from itertools import combinations
N, M = map(int, input().split())
numbers = map(int, input().split())

index = list(combinations(range(N-1), M))

for i in index:
    
