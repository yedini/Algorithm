from itertools import combinations
def solution(orders, course):
    cand = dict()
    answer = []
    for n in course:
        for order in orders:
            if len(order) >= n:
                l = list(combinations(list(order), n))
                for ll in l:
                    print(type(ll))
                    if ll in cand.keys():
                        cand[ll] += 1
                    else:
                        cand[ll] = 1
    for key, value in cand.items():
        if value >= 2:
            answer.append(key)
    return ll