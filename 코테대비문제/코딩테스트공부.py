# 참고: https://velog.io/@0_hun/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%BD%94%EB%94%A9-%ED%85%8C%EC%8A%A4%ED%8A%B8-%EA%B3%B5%EB%B6%80-2022-KAKAO-TECH-INTERNSHIP-Level-3-Python

# dp[i][j]: 알고력 i, 코딩력 j를 도달할 수 있는 최단시간
# dp[alp][cop]=0을 시작으로 dp배열을 채워나감.
def solution(alp, cop, problems):
    # 해결해야될 알고, 코딩 중 가장 큰 값 구하기
    max_alp, max_cop = 0, 0
    for p in problems:
        max_alp = max(p[0], max_alp)
        max_cop = max(p[1], max_cop)
    dp = [[float('inf')] * (max_cop+1) for _ in range(max_alp + 1)]
    
    # 목표값을 넘으면 안된다!
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    dp[alp][cop]=0
    
    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i>= alp_req and j >= cop_req:
                    # 둘 중 하나라도 목표값을 넘어가면 안됨!
                    new_alp = min(i+alp_rwd, max_alp)
                    new_cop = min(j+cop_rwd, max_cop)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j]+cost)
            
    return dp[max_alp][max_cop]