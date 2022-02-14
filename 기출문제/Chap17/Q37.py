INF = int(1e9)
n = int(input())
m = int(input())

# 2차원 리스트
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용: 0으로 초기화
for a in range(1, n+1):
    graph[a][a] = 0

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

# 플로이드 워셜 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()     # 한줄 띄는 역할