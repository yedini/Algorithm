N = int(input())

dp = [0] * 1001

dp[1] = 1   # 돌이 1개: 한번만에 끝남
dp[2] = 2   # 돌이 2개: 두번만에 끝남
dp[3] = 1   # 돌이 3개: 한번만에 끝남

for i in range(4, N+1):
    if dp[i] % 3 == 1:
        dp[i] = dp[i-i//3] + 1
    elif dp[i] % 3 == 2:
        dp[i] = dp[i-i//3] + 2
    else:
        dp[i] = dp[i-3] + 1

# 홀수번 한거면 상근, 짝수번 한거면 창영이 이김
if dp[N] % 2 == 1:
    print("SK")
else: print("CY")
