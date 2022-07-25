from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic = defaultdict(list) # defaultdict: key에 대한 value를 안주면 default 값을 value로 설정하는 함수. list를 인자로 넣었으므로 빈 리스트가 default로 생성된다
    
    # 해당될 수 있는 모든 query를 score와 함께 기록
    for i in info:
        i = i.split()
        condition = i[:-1] # 점수빼고
        score = int(i[-1])
        for i in range(5):
            case = list(combinations([0, 1, 2, 3], i)) # -가 들어갈 수 있는 위치에 대한 조합
            for c in case:
                temp = condition.copy()
                for idx in c:
                    temp[idx] = "-"
                key = ''.join(temp)
                dic[key].append(score)
    
    # score가 높은 순으로 정렬
    for value in dic.values():
        value.sort()
    
    for q in query:
        q = q.replace("and ", "")
        q = q.split()
        target_key = ''.join(q[:-1])
        target_score = int(q[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            # score 순으로 sort 되어있음
            # -> bisect_left로 더 작은 값의 마지막 인덱스를 찾고
            # 전체 개수에서 그 인덱스 뺀만큼의 개수가 해당 count가 됨
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)
    return answer