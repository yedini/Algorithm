def solution(people, limit):
    answer = 0
    people.sort()
    ##### Two Pointer 사용
    high = len(people)-1
    low = 0
    
    # index의 값이 작은값/큰값의 관계가 아닐 때까지 
    while low<=high:
        answer += 1   
        if people[low] + people[high] <= limit:
            # 작은값을 더했을 때 limit을 안넘을 경우 2명 태울 수 있음 -> 확인하는 포인터의 위치를 한칸 옮김
            low += 1 
        # 다음 단계에서는 그 다음 무거운 사람을 확인
        high -= 1
        
    return answer