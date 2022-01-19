nums = list(input())
nums = list(map(int, nums))
length = int(len(nums)/2)

if sum(nums[:length]) == sum(nums[length:]):
    print("LUCKY")
else: print("READY")
