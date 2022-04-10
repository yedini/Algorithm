def solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(num, idx):
        # nonlocal: 현재 지역변수가 아닌데 전역변수도 아닌 변수를 쓸 경우에 사용!
        nonlocal answer
        if idx == n:
            if num == target:
                answer += 1
            return
        else:
            dfs(num+numbers[idx], idx+1)
            dfs(num-numbers[idx], idx+1)
    
    dfs(0, 0)
    return answer