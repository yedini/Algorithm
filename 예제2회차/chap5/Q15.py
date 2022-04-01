from collections import deque
n, m, k, x = map(int, input().split())

graph = [[0] for _ in range(n+1)]  #  도시별 연결된 도시 정보
for _ in range(m):
    i, o = map(int, input().split())
    graph[i].append(o)


dist = [0]*(n+1)  # 도시별 출발도시로부터의 최단거리     -> -1로 넣어서 visited 안만드는 대신 dist가 -1이냐로 방문여부 확인할수도 있음!
visited = []  # 방문한 곳 저장
q = deque()
q.append(x)
dist[x] = 0  # 출발 지점의 최단거리는 0
visited.append(x)
while q:
    i = q.popleft()  # 현재 위치

    for new in graph[i]:  # 현재 위치에서 갈 수 있는 도시들
        if new not in visited:   # 아직 방문 안한 곳이면 방문하기
            q.append(new)
            dist[new] = dist[i]+1  # 현재 위치 +1 로 출발도시로부터의 최단거리를 기록
            visited.append(new)


if k not in dist:
    print(-1)
else:
    for i in range(1, len(dist)):
        if dist[i] == k:
            print(i)
