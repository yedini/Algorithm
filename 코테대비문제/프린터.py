def solution(priorities, location):
    answer = 0
    l = [(j, i) for i, j in enumerate(priorities)]
    
    while True:
        temp = l.pop(0)
        if l and temp[0] < max(l)[0]:     # 더 안남아있을 수도 있어서?
            l.append(temp)
        else:
            answer += 1
            if temp[1] == location:
                break
    return answer