# M*2+N 크기에 보드를 만들고 중앙에 자물쇠를 배치
# key를 4번 돌려가며 차례로 이동
# 위에서 아래로 열쇠를 이동했을 때 중앙의 키가 모두 1이 되면 풀림

# 열쇠를 자물쇠 위에 넣어보는 함수
def attach(x, y, M, key, board):  
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += key[i][j]
            
# 열쇠를 빼는 함수(안맞으면 다시 돌려놔야하므로)
def detach(x, y, M, key, board):
    for i in range(M):
        for j in range(M):
            board[x+i][y+j] -= key[i][j]
            
# 90도 회전하는 함수
def rotate90(arr):
    return list(zip(*arr[::-1])) 
    # *의 역할: column별로 묶이게
    # ::의 역할: 처음부터 끝까지 -1칸 간격으로(역순으로)

# 모두 1인지 확인하는 함수
def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M+i][M+j] != 1:
                return False;
    return True
    

def solution(key, lock):
    M, N = len(key), len(lock)
    
    board = [[0] * (M*2+N) for _ in range(M*2+N)]
    
    # 자물쇠를 중앙에 배치
    for i in range(N):
        for j in range(N):
            board[M+i][M+j] = lock[i][j]
    
    rotated_key = key
    
    # 모든 방향 확인
    for _ in range(4):
        rotated_key = rotate90(rotated_key)
        for x in range(1, M+N):
            for y in range(1, M+N):
                # 열쇠 넣어보기
                attach(x, y, M, rotated_key, board)
                # 가능한지 확인하기
                if (check(board, M, N)):
                    return True
                #열쇠 빼기
                detach(x, y, M, rotated_key, board)
    return False