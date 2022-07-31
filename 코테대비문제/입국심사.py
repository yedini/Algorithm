# 참고: https://happy-obok.tistory.com/10
# 이분 탐색: 탐색 범위를 두 부분으로 분할해서 찾음 -> 정렬 필수
def solution(n, times):
    answer = 0
    # right: 가장 비효율적으로 심사했을 때 걸리는 시간 -> 가장 시간이 많이걸리는 심사관에게 n명이 모두 심사받는 경우.
    left, right = 1, max(times)*n
    while left <= right:
        mid = (left+right)//2 # 임의의 시간
        people = 0 # 모든 심사관이 mid분동안 심사한 사람의 수
        
        #mid 동안 심사한 사람 수가 받아야할 사람 수보다 많거나 같을 경우 -> 주어진 시간을 줄임 / 적은 경우는 시간 부족 -> 주어진 시간을 늘림
        for time in times:
            people += mid // time
            # 모든 심사관을 거치지 않아도 mid분동안 n명 이상의 심사를 할 수 있는 경우
            if people >= n: 
                break
        
        if people >= n:
            answer = mid
            right = mid - 1
        elif people < n:
            left = mid + 1
            
    return answer