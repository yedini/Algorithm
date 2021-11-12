n, m = map(int, input().split())

# 맵 정보
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    
    # 종료조건: 범위를 벗어날 때
    if x >= n or x <= -1 or y >=m or y<= -1:
        return False
    
    # 아직 방문하지 않은 경우
    if graph[x][y] == 0:
        graph[x][y] = 1

        # 재귀적 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    
    return False

# 한 묶음인 얼음 새기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)