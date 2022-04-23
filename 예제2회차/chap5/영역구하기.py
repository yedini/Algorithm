m, n, k = map(int, input().split())
graph = [[0]*n for _ in range(m)]

# 도형이 있는 칸 표시
for _ in range(k):
    xs, ys, xe, ye = map(int, input().split())
    for i in range(ys, ye):
        for j in range(xs, xe):
            graph[i][j] = 1    # 1: 칠해진 구간

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(y, x, a):   # y, x, 넓이
    graph[y][x]=1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx>=0 and nx<n and ny>=0 and ny<m and graph[ny][nx] == 0:
            a = dfs(ny, nx, a+1)   
    return a # a가 함수의 return & 함수 내부에서 dfs return값을 a에 저장 -> count

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(dfs(i, j, 1))


print(len(result))
print(*sorted(result))