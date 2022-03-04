n = int(input())
nums = list(map(int, input().split()))
nums.sort()

target = 1

for i in nums:
    if target < i:
        break
    target += i

print(target)