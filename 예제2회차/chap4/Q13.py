from itertools import combinations
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 집과 치킨집 위치 저장
c = []
h = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            c.append((i, j))
        elif graph[i][j] == 1:
            h.append((i, j))

# 폐업안시킬 m개의 치킨집 조합 리스트 생성
coms = list(combinations(c, m))

answer = 1000000  # 최종 답: 폐업안시킬 치킨집 조합 중 가장 치킨 거리가 짧은 조합의 치킨거리
for clist in coms:  # 모든 조합에 대해 확인
    cdist = 0       # 한 조합의 최소 치킨거리
    for home in h:  # 집마다 가장 가까운 치킨집과의 거리 확인
        hdist = 100000
        for d in clist:
            hdist = min(hdist, abs(home[0]-d[0])+abs(home[1]-d[1]))
        cdist += hdist
    answer = min(answer, cdist)

print(answer)

