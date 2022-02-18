def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split()) # 노드, 간선 개수 input
parent = [0] * n   # 부모테이블 초기화
edges = []    # 모든 간선을 담을 리스트

# 부모를 자기자신으로 초기화
for i in range(n):
    parent[i] = i 
