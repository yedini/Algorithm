from collections import deque
def solution(x, y, n):
    answer = []
    dist = [-1]*1000001
    q = deque()
    q.append(x)   # 현재 숫자, 변환 횟수
    dist[x] = 0
    while q:
        now = q.popleft()
        # 3 곱하기
        for c in [now*3, now*2, now+n]:
            if c <= 1000000 and dist[c] == -1:
                dist[c] = dist[now]+1
                q.append(c)

    return dist[y]