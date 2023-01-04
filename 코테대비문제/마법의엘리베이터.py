def solution(storey):
    answer = 0
    
    while storey:
        r = storey % 10
        # 나머지가 6에서 9 사이인 경우
        if r > 5:
            answer += (10-r)
            storey += 10
        # 나머지가 0에서 4
        elif r < 5:
            answer += r
        # 나머지가 5 --> 다음 자리 수에 따라 결정
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += r
        
        # 현재 일의 자리 수를 해결했으므로 없애기
        storey //= 10
        
    return answer