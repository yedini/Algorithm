N, M = map(int, input().split())  

# 무게별 빈 리스트 만들기
w = [0] * (M+1)

weights = list(map(int, input().split()))

# 무게별 개수 새기
for i in weights:
    w[i] += 1

result = 0

for i in range(1, M+1):
    N -= w[i]    # i번째 무게에 해당하는 공을 제외한 공의 개수
    result += w[i] * N  # 나머지 개수만큼 짝이 가능함.

print(result)