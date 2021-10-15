N = int(input())
t = list(map(int, input().split()))

t.sort()

t_sum = [sum(t[:i+1]) for i in range(len(t))]

print(sum(t_sum))
