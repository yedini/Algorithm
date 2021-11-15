N = int(input())
p = int(input())

graph = [[]*N for _ in range(N+1)] # N개의 원소를 갖는 빈 list가 N+1개

for _ in range(p):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count=0
visited = [0] * (N+1)

def dfs(start):
    global count
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            count += 1

dfs(1)
print(count)
