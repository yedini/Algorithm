n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

first = nums[n-1]
second = nums[n-2]

# 가장 큰 수가 더해지는 횟수 세기
# 수가 더해지는 형태: k + 1 길이의 수열이 반복됨
# => m//(k+1) 만큼 수열이 반복되고, m을 k+1로 나눴을 때의 나머지만큼 가장 큰수가 추가로 반복

count = int(m/(k+1)) * k   # m/(k+1)번 수열이 반복 => 제일 큰수는는 m/(k+1) * k 번 반복
count += m % (k+1)

result = count * first
result += (m-count) * second

print(result)