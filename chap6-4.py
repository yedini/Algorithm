N, K = map(int, input().split())

A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i] = B[i]
    else:
        break

print(sum(A))

