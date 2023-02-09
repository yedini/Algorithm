def solution(order):
    answer = 0
    stack = []   # 보조 벨트
    start = 1    # 컨베이어 벨트 위에 있는 택배 번호 중 가장 작은 숫자
    end = len(order)  # 택배 번호 중 가장 큰 숫자
    
    for n in order:
        # 컨베이어 벨트 위에 택배가 없거나, 실어야할 숫자가 베이어 벨트의 가장 낮은 숫자보다 작을 경우
        if start > end or n < start:
            # 보조 벨트의 마지막 숫자와 같은 숫자 -> 택배 싣기
            if n == stack[-1]:
                stack.pop()
                answer += 1
            
            # 아닐 경우 -> 더 이상 트럭을 채울 수 없음.
            else:
                break
                
        # 숫자가 컨베이어 벨트의 가장 낮은 숫자보다 클 경우   
        else:
            stack = stack + list(range(start, n))
            start = n+1
            answer += 1
   
    return answer