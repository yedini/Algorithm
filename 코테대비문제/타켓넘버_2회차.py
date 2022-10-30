def solution(numbers, target):
    answer = 0
    def dfs(n, s):  # 현재 계산한 횟수, 현재 합
        nonlocal answer
        if n == len(numbers):
            if s == target:
                answer += 1
        else:
            dfs(n+1, s+numbers[n])
            dfs(n+1, s-numbers[n])
    dfs(0, 0)        
    return answer