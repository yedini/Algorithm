n = int(input())

count = 0  # 거스름돈 개수 count
while n > 0:      # 거스름돈이 0이 될때까지
    if n in [1, 3]:  # 5원/2원으로 해결할 수 없는 경우: 1원이나 3원
        count = -1
        break
    elif n >=10:  # 10 이상일 경우 짝/홀수 상관없이 -5
        n -= 5
    
    elif n % 2 == 1: # 10 미만이면서 홀수, 1/3이 아님: 5를 뺄 수 있음
        n -= 5
    else:    # 10 미만이면서 짝수:5를 빼면 0으로 못만듦 -> -2 
        n -= 2
    count += 1    

print(count)