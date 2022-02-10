n = int(input())

# 입력 맵 가져오기
dp = []
for i in range(n):
    dp.append(list(map(int, input().split())))

# 맵에다 각 위치별로 최대로 합해질 수 있는 값 구하기
for i in range(1, n):
    for j in range(len(dp[i])):
        # 해당 층의 첫번째 값이면: 무조건 위층의 첫번째 값이 더해짐
        if j == 0:
            dp[i][j] = dp[i][j]+dp[i-1][0]
        # 해당 층의 마지막 값이면: 무조건 위층의 마지막 값이 더해짐
        elif j == len(dp[i])-1 :
            dp[i][j] = dp[i][j]+dp[i-1][len(dp[i])-2]
        # 위의 두 경우가 아닌 경우: 위층의 대각선 왼쪽, 오른쪽 값중 더 큰 값이 더해짐
        else:
            dp[i][j] = dp[i][j]+ max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[n-1]))
