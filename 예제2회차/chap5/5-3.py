n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    # 범위를 벗어날 때: 종료
    if x >= n or x <0 or y >= m or y < 0:
        return False
    
    # 아직 방문 안한 빈칸일경우: 방문으로 바꿔주고 다음 상하좌우 확인
    # -> 연결된 위치에 있는 빈칸을 다 하나로 보도록 함!
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

        return True  # 얼음을 얼린 칸을 찾았으므로 true 출력
    return False

# 묶음별로 count
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
