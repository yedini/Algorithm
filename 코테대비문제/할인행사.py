from collections import Counter
def solution(want, number, discount):
    answer = 0
    
    if len(discount) - 10 > 0:
        n = len(discount)-10+1
    else:
        n = 1
    
    for i in range(n):
        dic = Counter(discount[i:10+i])
        temp = True
        for j in range(len(want)):
            if dic[want[j]] != number[j]:
                temp = False
        if temp:
            answer += 1
            
    return answer