N = int(input())
nums = list(map(int, input().split()))

def binarysearch(array, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid-1
        else:
            start = start+1
    return -1

result = binarysearch(nums, 0, N-1)
print(result)