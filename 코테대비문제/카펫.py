# (yellow가로*2)+(yellow세로*2) + 4 = brown
def solution(brown, yellow):
    answer = []
    
    yellow_x = 0
    yellow_y = 0
    
    # 노란색 개수만큼 반복
    for i in range(1, yellow+1):
        # i로 나눴을 때 나눠떨어지면 가로, 세로 지정
        if yellow % i == 0:
            yellow_x = int(yellow/i)
            yellow_y = i
            
            # 가로 세로 길이가 brown의 식과 맞으면 answer
            if yellow_x*2 + yellow_y*2 + 4 == brown:
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                
                # 가로가 더 길도록 sort
                return sorted(answer, reverse=True)
    return answer