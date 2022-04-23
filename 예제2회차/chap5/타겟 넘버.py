def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(num, idx):  # 더한 숫자, 현재 다루는 숫자의 위치
        # nonlocal: 현재 지역변수가 아닌데 전역변수도 아닌 변수를 쓸 경우에 사용!
        nonlocal answer
        if idx == n:  # n개 다 더했을 때 target값과 같으면 answer +=1
            if num == target:
                answer += 1
            return  # 현재 함수 밖의 지역변수 answer에 원하는 값을 저장 -> 별다른 값을 return하지 않음
        else:
            # 해당 위치의 숫자를 더하거나 빼는 것으로 dfs
            dfs(num+numbers[idx], idx+1) 
            dfs(num-numbers[idx], idx+1)
    
    dfs(0, 0)
    return answer