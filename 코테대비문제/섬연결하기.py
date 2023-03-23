def solution(n, costs):
    answer = 0
    # 비용을 기준으로 오름차순 정렬
    costs.sort(key = lambda x: x[2])
    
    # 연결된 섬 - 최소비용인 간선의 출발지에서부터 시작
    node = set([costs[0][0]])
    
    # 크루스칼 알고리즘
    while len(node) != n:
        for cost in costs:
            # 출발, 도착 모두 node에 있는 경우 -> 이미 낮은 비용으로 연결 완 -> 패스
            if cost[0] in node and cost[1] in node:
                continue
            # 둘 중 하나가 연결되어 있을 경우 -> 연결 -> node에 추가, answer에 비용 추가
            elif cost[0] in node or cost[1] in node:
                node.update([cost[0], cost[1]])
                answer += cost[2]
                break # 연결 -> for문 멈추고 다 연결됐는지 확인 -> 안됐으면 반복 
    
    return answer