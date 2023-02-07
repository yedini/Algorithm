def solution(n):
    answer = [[0]*(i+1) for i in range(n)]  # 삼각형 틀 만들기
    
    # 3으로 나눴을 때 나머지가 0 -> 아래 방향
    #                      1 -> 오른쪽 방향
    #                      2 -> 위쪽 방향
    
    # answer 내 좌표 초기값
    x = -1
    y = 0
    
    # 채울 숫자의 초기값
    num = 1 
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1 # 높은 칸일수록 y수가 하나씩 적으므로 y에도 1을 빼줌
            answer[x][y] = num
            num += 1
    
    return sum(answer, [])