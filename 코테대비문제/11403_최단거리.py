# 플로이드워셜: 중간점(k)을 거쳐 도착점으로 가는 길이 있으면 1로 만들기
n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):   # i번째와 j번째 연결에 중간점 k가 존재하는지?
    for i in range(n):
        for j in range(n):
            if graph[i][k]==1 and graph[k][j]==1:
                graph[i][j]=1

for i in range(n):
    print(*graph[i])

