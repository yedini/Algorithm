# t가 미리 구할 숫자 개수 --> 전체 숫자는 t*m
def solution(n, t, m, p):
    temp = ''
    answer = ''
    numbers = '0123456789ABCDEF'
    for i in range(t*m):
        if i == 0:
            temp += '0'
        else:
            a = i   # 몫
            b = ''  # 나머지
            while a > 0:
                b = numbers[a%n]+b
                a = a // n
            temp += b
    
    # 튜브가 말할 숫자만 뽑기
    for i in range(t):
        answer += temp[p-1+m*i]
    return answer