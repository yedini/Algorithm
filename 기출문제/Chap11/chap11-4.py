N= int(input())
c = list(map(int, input().split()))
c.sort()

target = 1
for i in c:
    if target < i:
        break
    target += i

print(target)