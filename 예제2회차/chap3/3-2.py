# 제일 큰 수를 k번, 두번째로 큰수를 1번 더하기
n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

first = nums[n-1]
second = nums[n-2]

result = 0
while True:             # break 걸릴때까지 계속 반복!
    for i in range(k):  # 첫번째 수 k번 더하기
        if m == 0:
            break       # m번만큼 다 더했으면 break
        m -= 1
        result += first
    
    # 제일 큰 수를 k번 더한 뒤 두번째 큰 수 한번 빼기
    if m == 0:
        break
    m -= 1
    result += second

print(result)

