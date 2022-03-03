n = int(input())
nums = list(map(int, input().split()))
nums.sort()

result = 1

for i in nums:
    if result < i:
        break
    result += i

print(result)