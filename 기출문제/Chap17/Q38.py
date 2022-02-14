INF = int(1e9)

# 노드, 간선 개수
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0
for a in range(1, n+1):
    graph[a][a] = 0

# 각 간선에 대한 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 학생별로 한명씩 확인하여 도달 가능한지 체크
result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1

print(result)