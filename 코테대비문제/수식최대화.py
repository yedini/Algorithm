from itertools import permutations

# 연산을 하는 함수
def op(op, n1, n2):
    if op == '+':
        return str(int(n1) + int(n2))
    elif op == '-':
        return str(int(n1) - int(n2))
    else:
        return(str(int(n1) * int(n2)))
    
def solution(expression):
    answer = 0
    ops = ['+', '-', '*']
    oplist = list(permutations(ops, 3))
    
    # 부호 정렬한 후보들에 대해 다 계산해서 그 결과를 cand에 넣기
    cand = []
    
    for opi in oplist:
        # expression을 숫자와 부호 단위로 잘라서 exp에 넣기
        exp = []
        temp = ''
        for e in expression:
            if e.isdigit():
                temp += e
            else:
                exp.append(temp) # 숫자
                exp.append(e)    # 부호
                temp = ''
        exp.append(temp) # 마지막 숫자

        for o in opi:
            stack = []
            while len(exp) != 0:
                temp = exp.pop(0)
                if temp == o:  # temp가 현재 for구문에 해당하는 부호면
                    stack.append(op(o, stack.pop(), exp.pop(0))) # 다음 숫자와 연산 수행
                else:   # 아니면 stack에 다시 더하기
                    stack.append(temp)
            # 아직 연산 안이루어진 숫자 및 부호: for 구문의 다음 차례에서 계산되기 위해 exp로 저장
            exp = stack 
        cand.append(abs(int(exp[0])))
    return max(cand)