from collections import deque
def bfs(begin, target, words, visited):
    queue = deque()
    queue.append([begin, 0])
    
    while queue:
        word, cnt = queue.popleft()
        if word == target:
            return cnt
        # 한글자만 다를 경우 queue에 넣기
        for i in range(len(words)):
            temp_cnt = 0
            if not visited[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    queue.append([words[i], cnt+1])
                    visited[i] = True

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    visited = [False]*len(words)
    answer = bfs(begin, target, words, visited)
    return answer