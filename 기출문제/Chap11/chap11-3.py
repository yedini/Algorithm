nums = input()

# 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우를 고려
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

#첫번째 원소
if nums[0] == '0':
    count1 += 1
else:
    count0 += 1

# 두번째 원소부터 바뀌는지 각각 확인
for i in range(1, len(nums)):
    if nums[i-1] != nums[i]:
        if nums[i] == '0': # 새로운 값이 0이면 1로 바꿔줘야 하므로 count1에 1을 더한다.
            count1 += 1
        else:
            count0 += 1

print(min(count0, count1))