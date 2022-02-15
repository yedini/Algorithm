# https://blex.me/@mildsalmon/chap-17-%EC%B5%9C%EB%8B%A8%EA%B2%BD%EB%A1%9C-q39-%ED%99%94%EC%84%B1-%ED%83%90%EC%82%AC
# 다익스트라 알고리즘 활용: 매 단계마다 방문하지 않은 노드 중 최단거리가 가장 짧은 노드를 확인
#  : 우선순위 큐 활용
import heapq
INF = int(1e9)
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for tc in range(T):
    n = int(input())
    
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    # 최단거리 테이블 - 초기화
    distance = [[INF] * n for _ in range(n)]

    # (0, 0)에서 시작
    x, y = 0, 0
    # 큐에 (비용, x위치, y위치) 순서의 튜플 삽입
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    # 다익스트라 알고리즘
    while q:
        # 최단거리가 가장 짧은 노드 꺼내기
        dist, x, y = heapq.heappop(q)
        # 처리된 적이 있는 노드는 넘기기
        if distance[x][y] < dist:
            continue
        # 현재 노드와 연결된 다른 노드 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵의 범위를 벗어날 경우 무시
            if nx <0 or nx>=n or ny<0 or ny>=n:
                continue
            cost = dist+graph[nx][ny]   # 원래 위치의 비용 + 이동한 위치의 비용
            # 현재 노드를 거쳐 다른 노드로 이동하는 거리가 짧은 경우
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))
    
    print(distance[n-1][n-1])