from collections import deque
n = int(input())
p = int(input())

graph = [[] for _ in range(n+1)]  # 컴퓨터별 연결 컴퓨터 표시
for _ in range(p):
    l, r = map(int, input().split())
    graph[l].append(r)
    graph[r].append(l)

q = deque()
visited = [1]
q.append(1)
count = 0
while q:
    d = q.popleft()
    for next in graph[d]:
        if next not in visited:
            visited.append(next)
            q.append(next)
            count += 1

print(count)