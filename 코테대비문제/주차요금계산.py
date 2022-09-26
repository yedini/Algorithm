from collections import defaultdict
import math 

def solution(fees, records):
    answer = []
    d = dict()
    total = defaultdict(int)
    
    # 시간 기록
    for record in records:
        time, num, state = record.split()
        h, m = map(int, time.split(":"))
        time = h*60+m
        if num in d:
            total[num] += time-d[num]
            del d[num]
        else:
            d[num] = time
            
    # 출차 안한 경우
    maxtime = 23*60 + 59
    for num, t in d.items():
        total[num] += maxtime - t
        
    # 요금 계산
    f0, f1, f2, f3 = fees
    for num, t in total.items():
        cost = f1
        if t > f0:
            cost += math.ceil((t-f0)/f2)*f3
        answer.append((num, cost))
    answer.sort()
    return [value[1] for value in answer]