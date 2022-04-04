# 순열을 이용해서 완전탐색
from itertools import permutations

n = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))
op_num = list('+'*op[0]+'-'*op[1]+'*'*op[2]+'/'*op[3])  
op = permutations(op_num, n-1)  # 연산자중에서 n-1개만큼 뽑기
op = list(set(op))          # 중복 제거


# 최소, 최대값 초기화
min_value = 1e9
max_value = -1e9

# 연산자 순서 후보 개수만큼 완전탐색
for i in op:
    result = A[0]
    for j in range(n-1):
        if i[j] == '+':
            result += A[j+1]
        if i[j] == '-':
            result -= A[j+1]
        if i[j] == '*':
            result *= A[j+1]
        if i[j] == '/':
            result = int(result/A[j+1])
    max_value = max(max_value, result)
    min_vaule = min(min_value, result)

print(max_value)
print(min_value)  # 왜 최소값이 이상하게 나올까??~?~?~
