# solution1 - 내 풀이: 효율성 x
def solution1(board, skill):
    answer = 0
    for s in skill:
        # 공격
        for i in range(s[1], s[3]+1):
            for j in range(s[2], s[4]+1):
                if s[0] == 1:
                    board[i][j] -= s[5]
                else:
                    board[i][j] += s[5]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 0:
                answer += 1
    return answer

# solution2 - 누적합 : 사용효율성 o
# 누적합 사용
def solution2(board, skill):
    answer = 0
    temp = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        temp[r1][c1] += degree if type ==2 else -degree
        temp[r1][c2+1] += -degree if type==2 else degree
        temp[r2+1][c1] += -degree if type==2 else degree
        temp[r2+1][c2+1] += degree if type==2 else -degree
    
    # 행 기준 누적합
    for i in range(len(temp)-1):
        for j in range(len(temp[0])-1):
            temp[i][j+1] += temp[i][j]
    
    # 열 기준 누적합
    for j in range(len(temp[0])-1):
        for i in range(len(temp)-1):
            temp[i+1][j] += temp[i][j]
    
    # 기존 배열과 합치기
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += temp[i][j]
            if board[i][j] >0:
                answer +=1
    return answer