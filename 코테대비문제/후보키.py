from itertools import combinations

def solution(relation):
    answer = 0
    l = len(relation)
    relation = list(zip(*relation))  # 행과 열 바꾸기
    for i in range(1, l+1):
        if len(relation) >= i:
            cand = list(combinations(range(len(relation)), i))
            while cand:
                c = cand.pop(0)
                temp = [relation[j] for j in range(len(relation)) if j in c]
                if len(temp) > 0 and len(list(zip(*temp))) == len(set(zip(*temp))):
                    print(temp)
                    answer += 1
                    relation = [relation[j] for j in range(len(relation)) if j not in c]
                    cand = [cc for cc in cand if len(set(c).intersection(set(cc)))==0]
                    print(cand)
    return answer