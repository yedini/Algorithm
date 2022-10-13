from itertools import combinations
def solution(relation):
    new = list(zip(*relation))   # 행과 열 바꾸기
    cand = []
    for i in range(1, len(new)+1):
        cand = cand + list(combinations(range(len(new)), i))
    keys = []
    while cand:
        c = cand.pop(0)
        temp = [new[j] for j in range(len(new)) if j in c]

        # 유일성 확인
        if len(temp)>0 and len(list(zip(*temp))) == len(set(zip(*temp))):
            # 최소성 확인
            check = True
            for k in keys:
                if set(k).issubset(set(c)):   # k가 c의 부분집합인지 확인
                    check = False
                    break
            if check:
                keys.append(c)
    return len(keys)