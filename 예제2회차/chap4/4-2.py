l = input()
# 알파벳에 맞는 순서 지정
cols = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}

# a1 들어왔을 때 a:열, 1:행
r = int(l[1])
c = cols[l[0]]

# 움직일 수 있는 경우의 수
scenario = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

result=0

for s in scenario:
    nr = r+s[0]
    nc = c+s[1]

    # 체스 판 범위 내에 속하면 경우의 수로 인정
    if nr >=1 and nr <= 8 and nc >=1 and nc <=8 :
        result += 1

print(result)
