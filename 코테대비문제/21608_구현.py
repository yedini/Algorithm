n = int(input())
graph = [[0]*n for _ in range(n)]  # 배치할 테이블

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

students = {}
    
for _ in range(n**2):
    new = list(map(int, input().split())) #학생 번호와 좋아하는 친구
    like = new[1:]
    students[new[0]] = like  # students에 저장
    
    # 학생마다 배치가능한 후보들을 cand에 저장하고 나중에 정렬
    cand = []
    for i in range(n):
        for j in range(n):
            sum_like, sum_empty = 0, 0  #좋아하는친구 수, 빈칸 수
            if graph[i][j] == 0:
                for k in range(4):  #상하좌우 확인
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx >=0 and nx <n and ny >=0 and ny <n :
                        if graph[nx][ny] in like:
                            sum_like += 1
                        elif graph[nx][ny] == 0:
                            sum_empty += 1
                cand.append((sum_like, sum_empty, (i, j)))
    # # 친구 내림차순/빈칸 내림차순/ 위치 오름차순으로 정렬
    cand.sort(key=lambda x:(-x[0], -x[1], x[2])) 
    # 정렬 가장 첫번째 값의 i, j 위치에 저장
    graph[cand[0][2][0]][cand[0][2][1]] = new[0]


# 좋아하는 친구 수에 따른 호감도 계산
result = 0
for i in range(n):
    for j in range(n):
        temp = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx >=0 and nx <n and ny >=0 and ny <n:
                if graph[nx][ny] in students[graph[i][j]]:
                    temp += 1
        if temp != 0:
            result += (10**(temp-1))  # 10의 제곱수

print(result)
