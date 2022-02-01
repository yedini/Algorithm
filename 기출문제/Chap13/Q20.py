N = int(input())

graph= []
for i in range(N):
    graph.append(list(input().split()))

# 움직이는 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 0]

def teacher(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx and nx<N and 0<=ny and ny < N