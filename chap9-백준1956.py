import sys
INF = int(1e9)
V, E = map(int, input().split())

# graph 만들기: (V+1) X (V+1)
graph = [[INF]*(V+1) for _ in range(V+1)]

# 노드랑 노드길이 입력
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

# 플로이드 워셜 알고리즘
for k in range(1, V+1):
    for a in range(1, V+1):
        for b in range(1, V+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 가장 작은 cycle 거리(시작지점에서 다시 시작지점으로) 구하기-> 대각행렬값
cycle = INF
for i in range(V+1):
    cycle = min(cycle, graph[i][i])

if cycle >= INF:
    print(-1)
else:
    print(cycle)
