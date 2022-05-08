a, b, c, m = map(int, input().split())
hour = 24
tired = 0
work = 0

# 24시간이 다 지날때까지 쉬거나 일하기 반복
while hour > 0:
    hour -= 1
    if tired+a > m: # 현 상태에서 더 일했을 때 피로도가 m을 넘으면 안됨 -> 쉬자
        tired = max(0, tired-c)
    else:
        work += b
        tired += a

print(work)