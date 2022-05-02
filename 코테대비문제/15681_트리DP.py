n, r, q = map(int, input().split())
# 연결 관계 표시
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# i번째 노드가 루트인 서브트리의 정점 개수
subtree = [0]*(n+1)

# dfs: 제일 끝의 노드까지 들어간 뒤 나오면서 정점의 개수를 차례로 더함
def dfs(root):
    subtree[root] = 1
    for i in graph[root]:
        if not subtree[i]:
            dfs(i)
            subtree[root] += subtree[i]
    return

dfs(r)

for _ in range(q):
    print(subtree[int(input())])