from itertools import permutations
def solution(numbers):
    answer = 0
    cand = []
    # 만들 수 있는 모든 조합의 숫자를 만들고 unique한 리스트를 생성
    for n in range(1, len(numbers)+1):
        temp = list(set(permutations(list(numbers), n)))
        cand = list(set(cand+[int(''.join(i)) for i in temp]))
    
    # 0, 1: 소수에 해당 x
    for l in cand:
        if l in [0,1]:
            continue
        r = True

        # 자기자신까지의 숫자중 하나로라도 나눠지면 소수 x -> 멈추고 넘어감
        for v in range(2, l):
            if l % v == 0:
                r = False
                break
        if r:
            answer += 1
    return answer