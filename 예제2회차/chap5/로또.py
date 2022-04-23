from itertools import combinations
tc = []
while True:   # 입력값이 0일때까지 test case에 추가
    new = list(map(int, input().split()))
    if new == [0] :
        break
    tc.append(new)
    
for i in range(len(tc)):       # test case별로 가능한 조합 프린트
    nums = tc[i]
    k = nums.pop(0)            # 입력값 한 줄의 가장 첫번째 값은 k이므로 따로 뽑기
    ss = list(combinations(nums, 6))
    for s in ss:
        print(*s)
    
    if i != (len(tc)-1):    # test case 사이에 공백 프린트
        print(" ")
