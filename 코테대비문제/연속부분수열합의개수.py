def solution(elements):
    answer = []
    temp = elements+elements
    
    for i in range(1, len(elements)+1):
        for j in range(len(elements)):
            answer.append(sum(temp[j:j+i]))
    return len(set(answer))