T = int(input())
# test case 입력 => test case별로 값까지 계산하기
for tc in range(T):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 2차원 dp 테이블 만들기 (주어진 값이 2차원 map이니까!)
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index : index+m])  # 슬라이싱한 array가 추가됨 -> 행별로 삽입된다
        index += m
    
    # 다이나믹 프로그래밍
    for j in range(1, m):  # 열별로 값 채우기
        for i in range(n): 
            # 왼쪽 위에서 오는 값
            if i == 0:  # 1행일 경우 위에 값 없음 -> 0
                left_up = 0
            else: left_up = dp[i-1][j-1]  # 이전 열의 위에 값 가져오기
            
            #왼쪽 아래에서 오는 값
            if i == n-1:  # 마지막 행일 경우 밑에 값 없음 -> 0
                left_down = 0
            else: left_down = dp[i+1][j-1]  # 이전 열의 밑의 값 가져오기

            #왼쪽에서 오는 값
            left = dp[i][j-1]

            # 세 값 중 가장 큰 값이 기존 dp[i][j]에 더해짐
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)
    
    # 마지막 열의 값들 중 가장 큰 값이 최종 답
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)