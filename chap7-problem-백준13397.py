N, M = map(int, input().split())
numbers = map(int, input().split())

def binary(x):
    max_x = min_x = numbers[0]
    cnt = 1
    for i in numbers:
        max_x = max(max_x, i)
        min_x = min(min_x, i)
        if max_x - min_x > x:
            cnt += 1
            max_x = i
            min_x = i
    return cnt

start, end = 0, max(numbers)
result = 0
while start <= end :
    mid = (start-end) // 2
    if binary(mid) <= M:
        end = mid - 1
        result = mid
    else:
        start = mid + 1
    
print(result)

