# 균형잡인 괄호 문자열인 인덱스를 반환하는 함수
def balanced_index(p):
    count = 0  # 왼쪽괄호면 +1, 오른쪽이면 -1 -> 0이면 균형잡힌 것!
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
# 올바른 괄호 문자열인지 판단하는 함수
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우 False 반환 (??)
                return False
            count -= 1
    return True  # 쌍이 맞으면 true 반환

def solution(p):
    answer = ''
    # 빈 문자열일 경우 빈 문자열을 반환
    if p == '':
        return answer
    index = balanced_index(p)  # u와 v를 나누는 기준
    u = p[:index+1]
    v = p[index+1:]
    # u가 올바른 괄호 문자열 -> v에 대해서도 수행하고 결과 만들기
    if check_proper(u):
        answer = u + solution(v)
    # u가 올바른 괄호 문자열이 아닐 경우
    else:
        answer = '('  # 첫번째로 ( 붙이기
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫번째와 마지막 문자 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else: u[i] = '('
        answer += "".join(u)
    
    return answer