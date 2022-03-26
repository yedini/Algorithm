def solution(numbers, hand):
    answer = ''
    left=[1, 4, 7, 10]  # *를 10으로
    right=[3, 6, 9, 12] # #를 12로
    lhand = 10
    rhand = 12
    
    for i in range(len(numbers)):
        # 숫자가 0일경우 위치상 11과 같으므로 11로 변경
        if numbers[i] == 0:
            numbers[i] = 11
            
        if numbers[i] in left:   # left 안에 있을 경우 왼손
            answer = answer+'L'
            lhand = numbers[i]
        elif numbers[i] in right: # right 안에 있을 경우 오른손
            answer = answer+'R'
            rhand = numbers[i]
        else:
            # 현재 위치와 눌러야될 숫자 사이 거리 구하기
            #  => 두 숫자의 차이를 3으로 나눴을 때의 몫과 나머지를 더함
            ldist = abs(lhand-numbers[i])//3 + abs(lhand-numbers[i])%3
            rdist = abs(rhand-numbers[i])//3 + abs(rhand-numbers[i])%3
            
            # 더 가까운 쪽으로 누르기
            if ldist < rdist:
                answer = answer+'L'
                lhand = numbers[i]
            elif ldist > rdist:
                answer = answer+'R'
                rhand = numbers[i]
            
            # 거리가 같을 경우 왼손잡이/오른손잡이 여부에 따라 결정
            else:
                if hand == 'left':
                    answer = answer+'L'
                    lhand = numbers[i]
                else:
                    answer = answer+'R'
                    rhand = numbers[i]
    return answer