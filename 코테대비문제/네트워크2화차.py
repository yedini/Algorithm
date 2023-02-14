############# by dfs #############
def dfs(n, visited, i, computers):
    visited[i] = True 
    for c in range(n):
        if not visited[c] and computers[i][c] == 1:
            dfs(n, visited, c, computers)

def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(n, visited, i, computers)
            answer += 1
    return answer


############# by bfs #############
from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:   # i번째 컴퓨터를 아직 방문 안했을 때
            q = deque()
            q.append(i)
            while q:
                now = q.popleft()
                visited[now] = True
                for j in range(n):
                    if not visited[j] and computers[now][j] == 1:
                        q.append(j)
            answer += 1
    return answer