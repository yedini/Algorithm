from collections import deque

def bfs(node, tree, visited, wire, cnt):
    queue = deque()
    queue.append([node, tree, visited, wire])
    visited[node] = True
    
    while queue:
        node, tree, visited, wire = queue.popleft()
        cnt += 1
        
        for i in tree[node]: #원래 연결된 node들을 확인
            if not ((node==wire[0] and i == wire[1]) or (node == wire[1] and i == wire[0])):
                if not visited[i]:
                    visited[i] = True
                    queue.append([i, tree, visited, wire])
    return cnt

# 양방향 연결임을 고려해야 함!
def solution(n, wires):
    answer = 1e9
    tree = [[] for _ in range(n+1)]
    
    # 연결상태 확인하기
    for wire in wires:
        a, b = wire
        tree[a].append(b)
        tree[b].append(a)
    
    # 전선 하나씩 끊어보고 두 네트워크의 송전탑 개수 확인
    for wire in wires:
        visited = [False] * (n+1)
        temp = []
        for i in range(1, n+1):
            if not visited[i]:
                cnt = bfs(i, tree, visited, wire ,0)
                temp.append(cnt)
        # temp의 원소는 항상 2개
        answer = min(answer, abs(temp[0] - temp[1]))
        
    return answer