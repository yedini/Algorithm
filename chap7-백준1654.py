K, N = map(int, input().split())
lens = [int(input()) for _ in range(K)]

start = 0
end = max(lens)

while start <= end :
    mid = (start+end) // 2
    
    line = 0
    for i in lens:
        line += i//mid
    
    if line >= N :
        start = mid + 1
    
    else:
        end = mid - 1

print(end)