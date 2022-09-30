def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        a = i // n 
        b = i % n
        if a < b:
            a, b = b, a  # 둘 중 큰 값을 answer에 포함시킴
        answer.append(a+1)

    return answer