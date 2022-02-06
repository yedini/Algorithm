# 이진탐색 두번 -> target-1의 인덱스와 target+1의 인덱스 찾아서 빼기
#   => bisect 라이브러리 사용 : 쉽게 해결 가능!
from bisect import bisect_left, bisect_right
N, x = map(int, input().split())
nums = list(map(int, input().split()))


def bisec(array, left_val, right_val):
    left_idx = bisect_left(nums, left_val)
    right_idx = bisect_right(nums, right_val)
    return right_idx-left_idx

result = bisec(nums, x, x)
if result == 0:
    print(-1)
else: print(result)

