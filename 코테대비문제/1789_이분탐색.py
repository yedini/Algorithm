s = int(input())

# 최대로 더할 수 있는 수
# -> 제일 작은 수: 1부터 더해보고 s보다 커지면 n에서 1을 뺀다
n = 1
while n*(n+1)/2 <= s:
    n += 1

print(n-1)