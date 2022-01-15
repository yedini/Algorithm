N = int(input())
M = int(input())

# 부모테이블 초기화
parent = [0] * (N+1)

# 각 노드의 부모테이블을 자기자신으로 지정
for i in range(1, N+1):
    parent[i] = i

def get_parent(parent, x):
    if parent[x] != x:
        parent[x] = get_parent(parent, parent[x])
    return parent[x]

def get_union(a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

# 연결 컴퓨터와 비용 입력
l = []
for _ in range(M):
    a, b, c = map(int, input().split())
    l.append((c, a, b))

l.sort()

#최소비용 구하기
cost = 0
for i in l:
    c, a, b = i
    if get_parent(parent, a) != get_parent(parent, b):
        get_union(a, b)
        cost += c
    
print(cost)