def solution(n, edge):
    graph = [[] for _ in range(n+1)]    # 각 노드마다의 연결 여부 저장
    dist = [0 for _ in range(n+1)]      # 1번 노드에서 각 노드까지의 거리
    
    # graph에 연결 정보 저장
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    # 1번과 연결되어 있는 노드를 deque에 추가
    deque = []
    for i in graph[1]:
        deque.append((1, i))    # (1번 노드와의 거리, 노드 번호)
        
    # 1번 노드는 거리 계산이 필요 없으므로 1로 처리
    dist[1] = 1
    
    while len(deque) > 0:
        ndist, now = deque.pop(0)
        if dist[now] == 0:  # 아직 방문 x
            dist[now] = ndist
            for j in graph[now]:
                deque.append((ndist+1, j))
    
    return dist.count(max(dist))