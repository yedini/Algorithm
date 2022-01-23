import itertools

N, M = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(N)]

# 집, 치킨 위치 찾기
h = []
c = []
for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            h.append((i, j))   # 집이면 h에 저장
        elif map[i][j] == 2:
            c.append((i, j))   # 치킨집이면 c에 저장

# 폐업 안할 치킨집 조합 리스트 생성: combination 사용
x = list(itertools.combinations(c, M))

result = 999
for c in x:    # M개의 치킨집을 선택
    distance = 0
    for home in h:
        mindist = min([abs(home[1]-cc[1])+abs(home[0]-cc[0]) for cc in c])  # 집별로 가장 가까운 치킨집의 최소거리 구하기
        distance += mindist   #다 합치기
    result = min(result, distance)  # 최소값 구하기

print(result)




