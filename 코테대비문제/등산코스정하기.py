#참고: https://velog.io/@leejy1373/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EB%93%B1%EC%82%B0%EC%BD%94%EC%8A%A4-%EC%A0%95%ED%95%98%EA%B8%B0-Python
from collections import defaultdict
from heapq import heappop, heappush

def solution(n, paths, gates, summits):
    summits.sort()
    summits_set = set(summits)
    # 등산로 정보를 담은 dict 생성
    graph = defaultdict(list)
    for i, j, w in paths:
        graph[i].append((w, j))
        graph[j].append((w, i))
    
    def minint():
        pq = []  # (intensity, 현재 위치)
        visited = [10000001] * (n+1)
        
        # 모든 출발지를 우선순위 큐에 삽입
        for gate in gates:
            heappush(pq, (0, gate))
            visited[gate] = 0
        
        # 산봉우리에 도착할 때까지 반복
        while pq:
            intensity, node = heappop(pq)
            # 산봉우리이거나 더 큰 intensity이면 더이상 이용하지 않음.
            if node in summits_set or intensity > visited[node]:
                continue
            # 현재 위치에서 이동할 수 있는 곳을 큐에 추가
            for weight, next_node in graph[node]:
                # next_node에 더 작은 intensity로 도착할 수 있다면 큐에 넣지 않음.
                new_intensity = max(intensity, weight)
                if new_intensity < visited[next_node]:
                    visited[next_node] = new_intensity
                    heappush(pq, (new_intensity, next_node))
        
        # 구한 intensity 중 가장 작은 값을 반환
        min_intensity = [0, 10000001]  #[summit, intensity]
        for summit in summits:
            if visited[summit] < min_intensity[1]:
                min_intensity[0] = summit
                min_intensity[1] = visited[summit]
        return min_intensity
    
    return minint()