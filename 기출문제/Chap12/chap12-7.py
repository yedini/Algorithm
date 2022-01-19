nums = list(input())
nums = list(map(int, nums))
length = int(len(nums)/2)

if sum(nums[:length]) == sum(nums[length:]):     # 반 나눠서 길이 같으면 lucky 출력
    print("LUCKY")
else: print("READY")
