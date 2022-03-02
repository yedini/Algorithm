nums = list(input())
nums = list(map(int, nums))

result = nums[0]

for i in range(1, len(nums)):
    if result == 0 or result == 1 or nums[i] == 0 or nums[i] == 1:
        result += nums[i]
    else:
        result *= nums[i]

print(result)
