N, M = map(int, input().split())
tree = list(map(int, input().split()))

# start, end point 설정
start = 0
end = max(tree)

# 이진탐색
length = 0  # 나무의 총 길이

while start <= end :
    total = 0  # 잘린 나무길이
    mid = (start+end) // 2
    total = sum([t-mid for t in tree if t>mid])
    
    if total < M :  # 잘린 길이가 원하는 길이보다 적을 경우
        end = mid - 1

    else:  # 나무길이가 충분 -> 덜 자를 수 있을지 보기 위해 start를 늘림
        length = mid
        start = mid + 1

print(length)