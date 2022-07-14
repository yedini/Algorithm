from itertools import combinations
def solution(orders, course):
    answer = []
    for n in course:   
        cand = dict()     # 후보 메뉴구성 + 시킨 횟수를 cand에 담음
        for order in orders:
            if len(order) >= n:
                l = list(combinations(list(order), n))
                for ll in l:
                    lll = ''.join(sorted(ll))
                    if lll in cand.keys():
                        cand[lll] += 1
                    else:
                        cand[lll] = 1
        if cand:
            maxv = max(cand.values())  # cand에 담긴 후보 메뉴구성 중 가장 많이 나간 구성
            if maxv >= 2:  # 2번 이상 시킨 경우에만 해당!
                answer = answer + [k for k in cand.keys() if cand[k] == maxv] # answer에 메뉴구성을 추가
    return sorted(answer)