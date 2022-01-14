N, M = map(int, input().split())

parent = [0] * (N+1)
for i in range(N):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]

def get_union(a,b):           
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

roads = []
for _ in range(M):
    a, b, c = map(int, input().split())
    roads.append((c, a, b))

roads.sort()
result = 0
for i in roads:
    c, a, b  = i
    if parent[a] != parent[b]: # 사이클이 발생하지 않는 경우에만 집합에 포함
        get_union(a,b)
        result += c
        last = c

print(result-last)