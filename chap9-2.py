N, M = map(int, input().split())

INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

for a in range(1, N+1):
    graph[a][a] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1 # 양방향!

X, K = map(int, input().split())

# 플로이드 워셜 알고리즘
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


# 결과 출력
distance = graph[1][K] + graph[K][X]

if distance >= INF:
    print("-1")
else: print(distance)
