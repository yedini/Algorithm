#### 프로그래머를 통해 제출 필요 ####
from collections import deque

def get_next_pos(pos, board):  # 현재 위치, 보드
    next_pos = []  # 현재 위치에서 이동가능한 위치들
    pos = list(pos)  # set 형태를 list 형태로 바꾸기
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    
    # 이동경로 - 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        pos1_nx, pos1_ny, pos2_nx, pos2_ny = pos1_x+dx[i], pos1_y+dy[i], pos2_x+dx[i], pos2_y+dy[i]
        # 이동하는 두 칸이 모두 벽이 아니면 후보로 추가
        if board[pos1_nx][pos1_ny]==0 and board[pos2_nx][pos2_ny]==0:
            next_pos.append({(pos1_nx, pos1_ny), (pos2_nx, pos2_ny)})
    
    ## 회전
    # 현재 로봇이 가로
    if pos1_x == pos2_x:
        for i in [-1, 1]:  # 위쪽 또는 아래쪽 확인
            # 위가 모두 비어있을 경우: 위로 회전할 수 있는 두 경우를 후보에 추가
            if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})
                
    # 현재 로봇이 세로
    elif pos1_y == pos2_y:
        for i in [-1, 1]:  # 왼쪽 또는 오른쪽 확인
            # 옆이 모두 비어있을 경우: 옆으로 회전할 수 있는 두 경우를 후보에 추가
            if board[pos1_x][pos1_y+i]==0 and board[pos2_x][pos2_y+i]==0:
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})
    
    return next_pos  # 이동가능한 후보를 모두 담은 리스트 반환!
    
    
def solution(board):
    n = len(board)   # 보드의 크기 정의
    
    # 테두리에 벽을 다 세워서 로봇이 맵을 벗어나지 않는지에 대해 더 간단히 판단
    new_board = [[1]*(n+2) for _ in range(n+2)]
    # 테두리 제외한 칸에 원래 board의 값을 채워줌
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
            
    # BFS
    q = deque()
    visited = []
    pos = {(1,1), (1,2)}  # 로봇의 처음 위치를 튜플로 정의해서 set으로 묶음
    q.append((pos, 0))    # cost: 원점으로부터 걸리는 거리(비용)
    visited.append(pos)   # 방문 처리
    
    while q:    # q가 빌 때까지 반복
        pos, cost = q.popleft()
        # 로봇이 (n,n)에 도달한 경우 => 최단거리이므로 반환하기!
        if (n,n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치 => 큐에 삽입하고 방문처리
            q.append((next_pos, cost+1))  # 한칸 이동해서 얻은 후보이므로 cost에 +1
            visited.append(next_pos)
        
    #return 0