n = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())  # 연산자별 개수

# 최소, 최대값 초기화
min_value = 1e9
max_value = -1e9

# dfs 사용
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    # 모든 연산자를 다 사용한 경우, 최소값과 최대값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        if add > 0:
            add -= 1  # 덧셈 한번 사용
            dfs(i+1, now+A[i])
            add += 1  # 재귀 함수 이용해서 가능한 조합 다 써보고, 다 해봤으면 다시 개수 더하기
        
        if sub > 0:
            sub -= 1
            dfs(i+1, now-A[i])
            sub += 1

        if mul > 0:
            mul -= 1
            dfs(i+1, now*A[i])
            mul += 1

        if div > 0:
            div -= 1
            dfs(i+1, int(now/A[i]))
            div += 1

dfs(1, A[0])

# 최대값과 최소값 출력
print(max_value)
print(min_value)