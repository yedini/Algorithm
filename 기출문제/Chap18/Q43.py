def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split()) # 노드, 간선 개수 input
parent = [0] * (n+1)   # 부모테이블 초기화
edges = []    # 모든 간선을 담을 리스트

# 부모를 자기자신으로 초기화
for i in range(1, n+1):
    parent[i] = i 

# 간선 정보 입력받기
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 비용순 정렬
edges.sort()

total = 0
result = 0
# 간선을 하나씩 확인하면서 사이클이 발생하지 않는 경우에만 집합에 포함
for edge in edges:
    cost, a, b = edge
    total += cost
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost


print(total - result)
