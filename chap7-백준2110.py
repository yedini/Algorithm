N, C = map(int, input().split())
house = []
for i in range(N):
    house.append(int(input()))

house.sort()


# 집과 집 사이의 거리의 최솟값 1: start
start = 1
# 거리의 최대값: end
end = house[-1] - house[0]

result = 0
# 중간값 기준로 집 개수를 세서 
# C보다 크면 -> 최소값을 중간값 +1로
# C보다 작으면 -> 최대값을 중간값 -1로
# ==> 최소값이 최대값과 가까워질 때가지 반복

while start <= end:
    mid = (start+end) // 2
    old = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= old+mid : # 중간값 기준 집 개수보다 크면
            count += 1
            old = house[i]
    
    if count >= C :
        start = mid +1
        result = mid
    
    else:
        end = mid - 1

print(result)