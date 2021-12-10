N, M = map(int, input().split())
a = list(map(int, input().split()))


start = 0
end = max(a)

# 이진탐색
result = 0
while(start <= end) :
    total = 0
    mid = (start+end) // 2
    for x in a:
        # 잘랐을 때의 떡의 양
        if x > mid:
            total += x - mid

    # 떡 양 부족 -> 더 많이 자르기(왼쪽 탐색)
    if total < M :
        end = mid - 1
    
    # 떡 양 충분 -> 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid  # 최대한 덜 자른 값이 정답
        start = mid +1

print(result)


