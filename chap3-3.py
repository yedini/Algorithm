# 리스트 안에 한 행마다의 리스트를 갖도록 만들고, 
# 각 행에서의 최소값 추출해서 그 중 가장 큰 값 출력?
nrow, ncol = map(int, input().split())

mins = []
for i in range(nrow):
    row = list(map(int, input().split()))
    mins.append(min(row))

print(max(mins))