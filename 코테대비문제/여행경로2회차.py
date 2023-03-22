from collections import defaultdict

def dfs(n, path, graph, now):
    path.append(now)
    # path의 길이가 return이 가지는 길이와 똑같을 경우
    if len(path) == n+1:
        return True
    
    # 현재 출발지에서 갈 수 있는 도착지가 없는 경우(graph에 없는 경우) --> 다시 꺼냄
    if now not in graph:
        path.pop()
        return False
    
    # 현재 출발지에서 갈 수 있는 모든 도착점에 대해 확인
    for i in range(len(graph[now])):
        arr = graph[now][-1]
        graph[now].pop()
        
        if dfs(n, path, graph, arr):
            return True
        
        graph[now].insert(0, arr)
    
    path.pop()
    return False

def solution(tickets):
    answer = []
    # 출발지, 도착지 기록: 도착지가 겹치는 티켓이 있으므로 원소를 list로 갖는 defaultdict 생성
    graph = defaultdict(list)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
    
    # 도착지 list 정렬
    for k in graph.keys():
        graph[k].sort(reverse=True)
    
    n = len(tickets)
    path = []
    if dfs(n, path, graph, 'ICN'):
        answer = path
    return answer