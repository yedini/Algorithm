import heapq
N, M, start = map(int, input().split())
INF = int(1e9)

# 노드 정보 리스트
graph = [[] for _ in range(N+1)]
# 최단 거리 테이블
distance = [INF] * (N+1)

for _ in range(M):
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

def dij(start):
    q = []

    # 시작노드
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 알고리즘 수행
dij(start)

count = 0   # 도달할 수 있는 노드 개수
max_distance = 0 # 도달할 수 있는 노드 중 가장 멀리 있는 노드와의 최단거리
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드를 제외한 count 출력
print(count - 1 , max_distance)