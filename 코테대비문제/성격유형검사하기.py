def solution(survey, choices):
    answer = ''
    type = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(choices)):
        t1, t2 = survey[i][0], survey[i][1]
        if choices[i] <= 3:
            type[t1] += (4 - choices[i])
        elif choices[i] >= 5:
            type[t2] += (-4 + choices[i])
    
    types = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    for i, j in types:
        if type[i] >= type[j]:
            answer = answer + i
        else:
            answer = answer + j
    
    return answer