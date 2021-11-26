W = sorted([int(input()) for i in range(10)], reverse=True)[:3]
K = sorted([int(input()) for i in range(10)], reverse=True)[:3]

result = [0, 0]
for i in range(3):
    result[0] +=W[i]
    result[1] +=K[i]

result = [str(result[0]), str(result[1])]


print(" ".join(result))