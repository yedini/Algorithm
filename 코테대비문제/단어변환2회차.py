from collections import deque

def bfs(begin, target, words):
    visited = [False]*len(words)  # 각 단어 방문 여부
    wnum = len(begin) # 단어 길이
    q = deque()
    q.append([begin, 0])   # [현재 단어, 바뀐 횟수]
    
    while q:
        now, num = q.popleft()
        # target을 찾은 경우, 현재까지 바뀐 횟수를 return
        if now == target:
            return num
        for i in range(len(words)):
            if not visited[i] and sum([True if now[j]!=words[i][j] else False for j in range(wnum)])==1:
                q.append([words[i], num+1])
                visited[i] = True

                
def solution(begin, target, words):
    answer = 0
    # words 안에 target이 없는 경우 변환 불가 -> 0을 return
    if target not in words:
        return answer
    else:
        answer = bfs(begin, target, words)
    return answer