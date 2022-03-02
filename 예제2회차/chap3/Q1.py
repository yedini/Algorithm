n = int(input())
nums = map(int, input().split())
nums.sort()

result = 0 # 최종 그룹 수
count = 0  # 그룹별 count

for n in nums:
    count += 1
    if count >= n:  # 숫자보다 count가 크거나 같으면 한 그룹으로 묶기!
        result += 1
        count = 0   # count 초기화