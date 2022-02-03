from copy import deepcopy
from itertools import combinations

N = int(input())

graph= []
for i in range(N):
    graph.append(list(input().split()))

# 움직이는 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 0]


# 종류별로 위치 저장
empty = []
teacher = []
student = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'X':
            empty.append([i, j])
        elif graph[i][j] == 'T':
            teacher.append([i, j])
        elif graph[i][j] == "S":
            student.append([i, j])

# 만약 잡히면 T로 바꿈
def dfs(graph, x, y, idx):
    if x<0 or x>=N or y<0 or y>=N or graph[x][y] == 'O':
        return
    else:
        graph[x][y] = 'T'
        dfs(graph, x+dx[idx], y+dy[idx], idx)


def check():
    copy_board = deepcopy(graph)
    for [x, y] in teacher:
        for i in range(4):
            dfs(copy_board, x, y, i)
    # 원래 student를 새로 확인했을 때 한명이라도 S가 아니면 잡힌 것 -> False
    for [x, y] in student:
        if copy_board[x][y] != 'S':
            return False

    return True


for case in list(combinations(empty, 3)):
    for [x, y] in case:
        graph[x][y] = 'O'
    if check():
        print("YES")
        exit()
    for [x, y] in case:
        graph[x][y] = 'X'

print("NO")