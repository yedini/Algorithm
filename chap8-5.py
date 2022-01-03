N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [10001] * (M+1)

dp[0] = 0

for i in range(N):
    for j in range(arr[i], M+1):   #인덱스에 해당하는 값들을 수정
        if dp[j-arr[i]] != 10001:    # (i-k)원을 만드는 방법이 존재하는 경우
            dp[j] = min(dp[j], dp[j-arr[i]]+1)


# 결과 출력
if dp[M] == 10001:
    print(-1)
else: print(dp[M])
