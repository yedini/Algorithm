from collections import deque
def bfs(n, info):
    res = []  # 점수차가 최대로 나는 경우
    maxgap = 0
    q = deque()
    # 첫번째 숫자: focus(화살 쏘려는 숫자)
    q.append((0, [0,0,0,0,0,0,0,0,0,0,0]))
    
    while q:
        focus, arrow = q.popleft()
        
        # 화살을 다 쏜 경우
        if sum(arrow) == n: 
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10-i
                    else:
                        lion += 10-i
            # 라이언이 이길 경우
            if lion > apeach:
                gap = lion - apeach
                if maxgap > gap:
                    continue
                if maxgap < gap:
                    maxgap = gap
                    res.clear()
                res.append(arrow) # 같거나 크면 일단 추가
        # 화살을 더 쏜 경우(계속 어피치보다 많이 쏠경우 더 쏘게 될수도 있음)
        elif sum(arrow) > n:
            continue
        
        # 화살을 덜 쏜 경우(아직 화살 남았는데 10까지 간 경우)
        elif focus == 10:
            temp = arrow.copy()
            temp[focus] = n - sum(temp)
            q.append((-1, temp))
        # 화살쏘기
        else:
            # 어피치보다 한발 많이 쏘는경우
            temp = arrow.copy()
            temp[focus] = info[focus]+1
            q.append((focus+1, temp))
            # 0발 쏘는경우
            temp2 = arrow.copy()
            temp2[focus] = 0
            q.append((focus+1, temp2))
    return res
    
def solution(n, info):
    answer = bfs(n, info)
    if not answer:
        return [-1]
    elif len(answer) == 1:
        return answer[0]
    # 최대로 이기는 경우가 2개 이상: 가장 낮은 점수 있는걸로 맞춰야 함
    # 높은 점수부터 문제를 풀었으므로 가장 마지막 후보 선택
    else:
        return answer[-1]