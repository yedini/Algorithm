n = int(input())
sch = []
for _ in range(n):
    sch.append(list(map(int, input().split())))

# 정렬: 시작시간과 끝시간을 둘다 기준으로 삼음
sch = sorted(sch, key = lambda x: (x[1], x[0]))

# 정렬 후 가장 첫번째 회의부터 시작
# => 새로 확인한 회의의 시작시간이 현재 시작한 회의의 끝나는 시간보다 같거나 클 경우 그 회의 시작하기
count = 1
endtime = sch[0][1]
for i in range(1, n):
    if sch[i][0] >= endtime:
        count += 1
        endtime = sch[i][1]

print(count)  
print(sch) 