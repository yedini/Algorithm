N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(input()))

count = 0
def dfs(x,y):
    global count
    ## 종료조건
    # 범위를 벗어나거나 벽인 경우
    if x >= N or x <= -1 or y >=M or y<= -1 or graph[x][y]=="X":
        return False

    # 아직 방문하지 않은 경우
    if graph[x][y] == "O":
        graph[x][y] = 1
        
        # 재귀적 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        
        return True

    # 친구가 있는 경우
    if graph[x][y] == "P":
        graph[x][y] = 1
        count += 1
    # 재귀적 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        
        return True

    return False

for i in range(N):
    for j in range(M):
        if graph[i][j] == "I":
            graph[i][j] = "O"
            x = i
            y = j
            break
            
            
dfs(x,y)
if count == 0:
    count = "TT"
print(count)