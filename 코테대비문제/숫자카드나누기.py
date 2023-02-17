def solution(arrayA, arrayB):
    answer = 0
    # a 나눌 수 있고, b 나눌 수 없는 경우
    arrayA = set(arrayA)
    arrayB = set(arrayB)
    
    minA = min(arrayA)
    listA = [minA]
    for i in range(minA//2+1, 0, -1):
        if minA % i == 0:
            listA.append(i)
    
    for i in listA:
        a = [j % i for j in arrayA]
        b = [j % i for j in arrayB]
        if sum(a) == 0 and 0 not in b:
            answer = i
            break
            
    # a 나눌 수 없고 b 나눌 수 있는 경우
    minB = min(arrayB)
    listB = [minB]
    for i in range(minB//2+1, 0, -1):
        if minB % i == 0:
            listB.append(i)
            
    for i in listB:
        a = [j % i for j in arrayA]
        b = [j % i for j in arrayB]
        if sum(b) == 0 and 0 not in a:
            answer = max(answer, i)
            break
            
    return answer