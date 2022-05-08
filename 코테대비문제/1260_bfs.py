from collections import deque
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()  # 작은 번호부터 방문

visited1 = [False]*(n+1)
visited2 = [False]*(n+1)

# dfs
def dfs(start):
    print(start, end=' ')
    visited1[start] = True
    for i in graph[start]:
        if not visited1[i]:
            dfs(i)
            visited1[i] = True

# bfs
def bfs(start):
    q = deque()
    q.append(start)
    visited2[start] = True

    while q:
        now = q.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited2[i]:
                q.append(i)
                visited2[i] = True

dfs(v)
print()
bfs(v)