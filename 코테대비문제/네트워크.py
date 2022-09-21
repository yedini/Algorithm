# dfs 사용
def dfs(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[connect][com] == 1:
            if visited[connect] == False:
                dfs(n, computers, connect, visited)

def solution(n, computers):
    answer = 0
    visited = [False]*n
    for com in range(n):
        if visited[com] == False:
            dfs(n, computers, com, visited)
            answer += 1
    return answer


# bfs 사용
def bfs(n, computers, com, visited):
    visited[com] = True
    queue = []
    queue.append(com)
    while len(queue) != 0:
        com = queue.pop()
        visited[com] = True
        for connect in range(n):
            if connect != com and computers[connect][com] == 1:
                if visited[connect] == False:
                    queue.append(connect)

def solution2(n, computers):
    answer = 0
    visited = [False]*n
    for com in range(n):
        if visited[com] == False:
            bfs(n, computers, com, visited)
            answer += 1
    return answer