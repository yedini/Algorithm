N = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈

maximum = -1e9
minimum = 1e9

# 숫자 순서, 연산 합, 남은 더하기/빼기/곱하기/나누기 수
def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    # N번만큼 다했으면 최대값, 최소값 구하기
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:  # 합 연산 개수가 아직 남아있다면
        dfs(depth+1, total+nums[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total-nums[depth], plus, minus-1, multiply, divide) 
    if multiply:
        dfs(depth+1, total*nums[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total/nums[depth]), plus-1, minus, multiply, divide-1)

dfs(1, nums[0], opers[0], opers[1], opers[2], opers[3])
print(maximum)
print(minimum)
