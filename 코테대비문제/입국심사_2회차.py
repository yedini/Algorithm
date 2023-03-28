def solution(n, times):
    answer = 0
    start = min(times)
    end = max(times)*n # 걸릴 수 있는 최대 시간: 모든 사람이 제일 오래 걸리는 심사대에서 받을 때
    
    while start <= end:
        mid = (start+end) // 2
        
        # 임의의 시간동안 몇명을 검사할 수 있는지 확인
        pos = sum([mid//t for t in times])
                
        if pos >= n:
            answer = mid
            end = mid -1
            
        elif pos < n:
            start = mid + 1
            
    return answer