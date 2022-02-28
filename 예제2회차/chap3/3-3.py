# 행별로 최소값 찾기 -> 그중 최대값 찾기
n, m = map(int, input().split())

result = -1

for i in range(n):
    new = list(map(int, input().split()))
    minnum = min(new)
    result = max(result, minnum)

print(result)