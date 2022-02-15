###### ?????
import heapq
INF = int(1e9)
n, m = map(int, input().split())

start = 1  # 1번에서 시작
# 각 노드에 연결되어 있는 노드에 대한 정보
graph = [[] for i in range(n+1)] 
# 최단거리 테이블
distance = [INF] * (n+1)

# 간선 정보 입력받기
for _ in range(m):
    a,b = map(int, input().split())
    # 양방향 고려
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 최단 거리가 가장 짧은 노드 꺼내기
        dist, now  = heapq.heappop(q)
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

# 최단 거리가 가장 먼 노드 번호
max_node = 0
# 도달할 수 있는 노드 중 최단 거리가 가장 먼 노드와의 최단 거리
max_distance = 0
# 그 노드랑 동일한 최단거리를 갖는 노드 개수가 몇개인지
result = 0

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        resut = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))