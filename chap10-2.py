N, M = map(int, input().split())

parent = [0] * (N+1)   # 부모테이블 초기화

for i in range(N+1):   # 부모테이블을 자기 번호로 초기지정
    parent[i] = i

def find_parent(parent, x):   # 루트 노드 찾기
    if parent[x] != x:
        find_parent(parent, x)
    return parent[x]

def get_union(a,b):           # 팀 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b

def get_find(a,b):            # 같은 팀 여부 확인
    if parent[a] == parent[b]:
        print("Yes")
    else:
        print("No")

for _ in range(M):
    idx, a, b = map(int, input().split())
    if idx == 0:
        get_union(a,b)
    else:
        get_find(a,b)