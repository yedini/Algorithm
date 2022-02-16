n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n+1)
for i in range(0, n+1):
    parent[i] = i

for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(i):
        if nums[j] == 1:
            union_parent(parent, i+1, j+1)


check = list(map(int, input().split()))
# set에 parent node 넣어보고 확인(set은 중복이 안되므로)
parent_set = set()
for num in check:
    parent_set.add(parent[num])

if len(parent_set) == 1:
    print("YES")
else:
    print("NO")
    
