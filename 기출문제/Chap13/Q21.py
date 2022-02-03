from collections import deque

n, l, r = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0

# 특정 위치에서 출발 -> 모든 연합 체크 -> 데이터 갱신
def process(x, y, index):
    united = []  #(x,y) 위치와 연결된 나라(연합) 정보를 담는 리스트
    united.append((x,y))
    
    q = deque()
    q.append((x,y))

    union[x][y] = index  # 현재 연합 번호 할당
    summary = graph[x][y]  # 현재 연합의 전체 인구 수
    count = 1  # 현재 연합의 국가 수

    while q:  # q가 빌 때까지 반복 => BFS
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # -1: 아직 처리안한 경우만 고려
            if 0<=nx<n and 0<=ny<n and union[nx][ny] == -1:
                if l < abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))  # 연합에 추가
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))

    # 다 찾았으면 -> 연합 국가끼리 인구 분배
    for i, j in united:
        graph[i][j] = summary // count
    
    return count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:  # 해당 나라가 아직 처리 x
                process(i, j, index)
                index += 1

    # 모든 인구 이동이 끝난 경우
    if index == n*n:
        break
    total_count += 1

print(total_count)

