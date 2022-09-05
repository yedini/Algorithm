from itertools import permutations
def solution(k, dungeons):
    answer = -1
    clist = list(permutations(dungeons, len(dungeons)))
    for c in clist:
        now = k
        count = 0
        for i in c:
            if now < i[0]:
                break
            else: 
                now = now-i[1]
                count += 1
        answer = max(answer, count)
    return answer