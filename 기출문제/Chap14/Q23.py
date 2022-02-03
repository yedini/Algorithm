N = int(input())

scores = []
for _ in range(N):
    name, k, e, m = input().split()
    scores.append((name, int(k), int(e), int(m)))

scores = sorted(scores, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in scores:
    print(s[0])
