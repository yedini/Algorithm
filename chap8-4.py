N = int(input())

dp = [0] * 1000

dp[0] = 1
dp[1] = 3

for i in range(2, N):
    dp[i] = (dp[i-1] + dp[i-2]*2) % 796796

print(dp[N-1])