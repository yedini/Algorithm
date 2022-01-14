from collections import deque
import copy 

N = int(input())
indegree = [0] * (N+1)  # 모든 노드의 진입차수 초기화
graph = [[] for i in range(N+1)] # 각 노드에 연결된 간선 정보 그래프
time = [0] * (N+1)     # 각 강의의 시간

# 간선 정보 입력받기
for i in range(N+1):
    data = list(map(int, input().spilt()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] +=1
        graph[x].append(i)

# 위상정렬함수
def topology_sort():
    result = copy.deepcopy(time) # time 리스트의 값들을 복사해옴
    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, N+1):
        print(result[i])

topology_sort()
