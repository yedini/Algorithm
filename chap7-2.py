N = int(input())
n = sorted([int(n) for n in input().split()])

M = int(input())
m = [int(m) for m in input().split()]

def binarysearch(array, target, start, end):
    while start<=end:
        mid = (start+end) // 2
        
        if array[mid] == target:
            return "yes"
        
        elif array[mid] > target :
            end = mid - 1
        
        else:
            start = mid + 1
    
    return "no"

result = []

for r in m:
    result.append(binarysearch(n, r, 0, N-1))

print(" ".join(result))

