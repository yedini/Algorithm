import sys
N = int(input())

idx = [0]*10001 # input으로 들어올 수 있는 최대값만큼의 빈 리스트 만들기

# input 값에 해당하는 index에 1 더하기
for i in range(N):
    num = int(sys.stdin.readline())
    idx[num] = idx[num] + 1

# 해당 인덱스에 숫자가 들어있는 만큼 인덱스(=input number) 출력
for i in range(10001):
    if idx[i] != 0:
        for j in range(idx[i]):
            print(i)

