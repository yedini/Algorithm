N = int(input())
array = list(map(int, input().split()))

array.reverse()

dp = [1] * N
# 가장 긴 증가하는 부분 수열(LIS) 알고리즘
for i in range(1, N):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))
