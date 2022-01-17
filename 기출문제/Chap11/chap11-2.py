nums = list(input())
# 정수 형태의 개별값이 각각 들어있는 리스트 형태로 변경
nums = list(map(int, nums))

result = nums[0]
for i in range(1, len(nums)):
    if result <=1 or nums[i] <=1:
        result = result+nums[i]
    else:
        result = result*nums[i]

print(result)
