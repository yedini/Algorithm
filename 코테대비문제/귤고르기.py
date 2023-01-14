from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine).most_common()  #(해당 값, 횟수)
    
    while k > 0:
        c = counter.pop(0)
        answer += 1
        k -= c[1]
        
    return answer