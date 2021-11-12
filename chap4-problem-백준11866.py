N, K = map(int, input().split())

p = [i+1 for i in range(N)]  # 자리에 앉기
result = []

deletenum = 0   # 뺄사람 번호 초기값
while len(p) > 0 :
    deletenum += K   # 3번째 옆에 앉은 사람을 뺌
    deletenum = (deletenum-1) % len(p) # 뺄 사람 숫자가 사람 숫자보다 커질 수 있으므로 나눠주기
    popn=p.pop(deletenum)
    result.append(str(popn))

print("<"+", ".join(result)+">")