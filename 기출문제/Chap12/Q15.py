from collections import deque
N, M, K, X = map(int, input().split())

city = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    city[a].append(b)

distance = [-1] * (N+1)
distance[X] = 0
queue  = deque()
queue.append(X)

while queue:
    c = queue.popleft()
    for i in city[c]:
        if distance[i] == -1:
            distance[i] = distance[c] + 1
            queue.append(i)

check = False
for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)
        
        