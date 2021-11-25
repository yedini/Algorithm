N = int(input())
Numbers = sorted([int(input()) for i in range(N)], reverse=True)
Numbers = [str(n) for n in Numbers]
print(" ".join(Numbers))