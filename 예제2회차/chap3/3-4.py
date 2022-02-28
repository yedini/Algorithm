n, k = map(int, input().split())

result = 0
while True:
    # k로 나누어 떨어지는 n 만들기
    target = (n//k) * k
    # k로 나누어 떨어지는 target을 만든 만큼의 빼기 과정을 반영
    result += (n-target)
    # 빼기 완료 => 이제 n이 target이 됨
    n = target

    # n<k여서 나눌 수 없을 때 -> 반복문 탈출
    if n<k:
        break
    
    result += 1    ## ---> ???
    n // k

# n을 1인 상태로 만들도록 빼기
result += (n-1)
print(result)