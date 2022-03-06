n, m = map(int, input().split())

# 6으로 떨어지는 수만큼 세트+나머지 낱개 / 전부 세트(남더라도) / 전부 낱개 중 최소값 고르기
set = 10e9
one = 10e9
onlyset = 10e9
onlyone = 10e9

for _ in range(m):
    s, o = map(int, input().split())

    set = min(set, (n//6)*s)
    one = min(one, (n%6)*o)
    onlyset = min(onlyset, (n//6+1)*s)
    onlyone = min(onlyone, n*o)



print(min(set+one, onlyone, onlyset))