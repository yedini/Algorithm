from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    # 동일한 유저에 대해 한번의 신고기록만 남기기
    report = list(set(report))
    
    # list1: 각 user별로 신고한 user를 담는 dict
    # list2: 각 user별로 신고당한 횟수를 담는 dict
    list1 = dict()
    for i in id_list:
        list1[i] = []

    list2 = defaultdict(int)
    
    for i in report:
        f, t = i.split()
        list1[f].append(t)
        list2[t] += 1

    # k번 이상 신고당한 user의 이름을 d에 담음
    d = set([key for key, value in list2.items() if value >= k])
    
    # list1과 d가 겹치는 횟수를 세서 각 user별로 신고결과메일을 몇 통 받는지 count
    for key, value in list1.items():
        answer.append(len(set(list1[key]).intersection(d)))
        
    return answer