N = int(input())
Nnum = sorted(list(map(int, input().split())))
M = int(input())
Mnum = list(map(int, input().split()))

def binarysearch(array, target, start, end):
    while start<=end:
        mid = (start+end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return 0

for m in Mnum:
    print(binarysearch(Nnum, m, 0, N-1))
