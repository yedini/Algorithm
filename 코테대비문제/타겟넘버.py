########## bfs ##########
from collections import deque

def bfs(numbers, target):
    answer = 0
    queue = deque()
    queue.append([1, numbers[0]])  # 사용한 숫자 개수, 합
    queue.append([1, -numbers[0]])
    
    while queue:
        idx, s = queue.popleft()
        if idx == len(numbers):
            if s == target:
                answer += 1
        else:
            queue.append([idx+1, s+numbers[idx]])
            queue.append([idx+1, s-numbers[idx]])
    return answer
    
def solution(numbers, target):
    answer = bfs(numbers, target)
    return answer

########## dfs ##########
def solution(numbers, target):
    answer = 0
    def dfs(idx, nsum):
        nonlocal answer
        if idx == len(numbers):
            if nsum == target:
                answer += 1
            return
        else:
            dfs(idx+1, nsum+numbers[idx])
            dfs(idx+1, nsum-numbers[idx])
    dfs(0, 0)
    return answer