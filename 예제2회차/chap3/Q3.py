# 0을 뒤집는 경우와 1을 뒤집는 경우를 고려 => 더 작은 수가 답
nums = list(input())
nums = list(map(int, nums))

count0 = 0  # 전부 0으로 바꿀 때
count1 = 0  # 전부 1로 바꿀 때

# 첫번째 원소 확인
if nums[0] == 0:
    count1 += 1
else:
    count0 += 1

for i in range(1, len(nums)):
    if nums[i-1] != nums[i]:   # 전에꺼랑 다르면 count
        if nums[i] == 0:
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))