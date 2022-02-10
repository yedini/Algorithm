n = int(input())
t = []   # 각 상담을 완료하는데 걸리는 기간
p = []   # 각 상담을 완료했을 때 받는 금액
dp = [0] * (n+1)  # dp 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)


# 뒤쪽부터 현재 상담 일자의 이윤+현재 상담 마친 일자부터의 최대 이윤을 계산
# dp[i]: i번째날부터 마지막 날까지 낼 수 있는 최대 이익
# => 점화식: dp[i] = max(p[i]+dp[t[i]+i])
# max_value: 뒤에서부터 계산했을 때, 현재까지 최대 상담 금액

for i in range(n-1, -1, -1):   #거꾸로 확인
    time = t[i] + i  #현재 상담 마친 후 시점
    if time <= n:  #현재시점 상담이 전체 기간 내에 끝나는 경우
        dp[i] = max(p[i]+dp[time], max_value)
        max_value = dp[i]
    else:          #상담이 기간을 벗어나는 경우
        dp[i] = max_value

print(max_value)