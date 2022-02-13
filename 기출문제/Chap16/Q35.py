n = int(input())

ugly = [0] * n  # dp테이블
ugly[0] = 1     # 첫번째 못생긴 수 = 1

i2 = i3 = i5 = 0  # 기존 인덱스에 2, 3, 5배 취하기 위한 인덱스
next2, next3, next5 = 2, 3, 5   # 곱셈값 초기화

# 1부터 n까지 못생긴 수 찾기
for l in range(1,n):
    # 가능한 곱셈 결과 중 가장 작은 수를 선택
    ugly[l] = min(next2, next3, next5)

    # 인덱스에 따라 곱셈 결과를 증가
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

# n번째 못생긴 수를 출력
print(ugly[n-1])