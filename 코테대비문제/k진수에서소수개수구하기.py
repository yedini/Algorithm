# 1) 주어진 수 n을 k진수로 변경
# 2) 0 사이에 낀 숫자 추출
# 3) 낀 숫자 각각 소수인지 확인


def solution(n, k):
    answer = 0
    newn = ''
    temp = n
    # 1) 주어진 수 n을 k진수로 변경
    while temp:
        newn = str(temp % k) + newn
        temp = temp // k 
    
    # 2) 0 사이에 낀 숫자 추출 --> 하나씩 떼지 말고 split으로 나누자!!!
    
    primecand = newn.split("0")
    
    # 3) 숫자 각각 소수인지 확인
    for num in primecand:
        if num in ["0", "1", ""]:
            continue
        isprime=True
        for i in range(2, int(int(num)**0.5)+1):
            if int(num)%i == 0:
                isprime = False
                break
                    
        if isprime:
            answer += 1
    
    return answer