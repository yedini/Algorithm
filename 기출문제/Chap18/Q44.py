def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
parent = [0] * (n+1)  # 부모테이블 초기화
edges = []            # 모든 간선을 담을 리스트
result = 0            # 최종 비용을 담을 값

# 부모 노드를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# x, y, z 각 좌표 입력받기
x = []
y = []
z = []
for i in range(1, n+1):
    data = list(map(int, input().split()))
    x.append((data[0], i)) # 좌표값과 해당 위치 index를 튜플로 삽입
    y.append((data[1], i))
    z.append((data[2], i))

# 모두 정렬
x.sort()
y.sort()
z.sort()

# x, y, z 모두 인접한 노드들 사이의 간선 정보 추출
for i in range(n-1):
    # 두 노드 사이의 비용, 왼쪽 노드의 원래 위치, 오른쪽 노드의 원래 위치 순서대로 삽입
    edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))

# 간선정렬
edges.sort()

# 간선을 하나씩 확인하면서 사이클이 발생하지 않는 경우에만 집합에 포함
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost


print(result)