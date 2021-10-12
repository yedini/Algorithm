#### 실전문제 2 : 큰 수의 법칙 ####
N, M, K = map(int, input().split())
num = list(map(int, input().split()))

num.sort()   # 정렬

k = K
results = []
for i in range(M):
    if k != 0:
        results.append(num[-1])
        k -= 1
    else:
        results.append(num[-2])
        k = K

print(sum(results))
