# 왼쪽 0, 오른쪽 n개인 상태에서 하나씩 옮겨가며 확인
# Counter 사용
from collections import Counter
def solution(topping):
    answer = 0
    left =set()
    right = Counter(topping)
    left_num = 0
    right_num = len(right)
    for t in topping:
        right[t] -= 1
        
        if right[t] == 0:
            right_num -= 1
            
        if t not in left:
            left.add(t)
            left_num += 1
            
        if left_num == right_num:
            answer += 1
    return answer