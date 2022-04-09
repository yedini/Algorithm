from itertools import combinations
from copy import deepcopy
n = int(input())
graph = []
empty = []
teacher = []
student = []

for i in range(n):
    graph.append(list(input().split()))
    for j in range(n):
        if graph[i][j] == 'X':  # 장애물 세울 공간의 후보를 만들어야 하므로 빈칸 정보 저장
            empty.append((i, j))  
        elif graph[i][j] == 'T':
            teacher.append((i, j))
        else:
            student.append((i, j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cand = list(combinations(empty, 3))

# 주어진 방향에서 선생님이 확인 가능한 공간이면 T로 바꾸는 함수
def check(x, y, d):
    if x<0 or x>=n or y<0 or y>=n or temp[x][y] == 'O':
        return
    else:
        temp[x][y] = 'T'
        check(x+dx[d], y+dy[d], d)

result = 'NO'
for c in cand:
    temp = deepcopy(graph)
    for i in c:
        temp[i[0]][i[1]] = 'O'
    
    for t in teacher:
        for d in range(4):
            check(t[0], t[1], d)
    nows = [] 
    for s in student:
        # 학생 위치들을 확인해서 모두 그대로 S로 남아있는지 확인.
        nows.append(temp[s[0]][s[1]])
    if 'T' not in nows:
        result = 'YES'
        break

print(result)