def solution(targets):
    answer = 1
    targets.sort(key = lambda x: x[0])
    now = targets[0]
    for t in targets[1:]:
        if t[0] < now[1]:
            now = [t[0], min(now[1], t[1])]
        else:
            now = t
            answer += 1
    return answer